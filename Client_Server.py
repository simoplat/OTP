import hashlib
import datetime
import time

def calcola_valore_numerico(stringa_input: str) -> int:
    risultato_stringa = ""
    iterazione = 0
    tronca = 6
    for carattere in stringa_input:
        # La funzione ord() restituisce il valore Unicode del carattere (un INT)
        valore_numerico = ord(carattere)
        
        # 1. CONCATENAZIONE: Convertiamo il numero a stringa e lo concateniamo
        risultato_stringa += str(valore_numerico)
        
        iterazione += 1
        
        # 2. Limitiamo l'operazione ai primi 3 caratteri
        if iterazione == 100:
            break 
    risultato_stringa = risultato_stringa[:tronca]
    return int(risultato_stringa)


def generate_hash():
    # --- LOGICA DI HASHING AGGIORNATA PER INTERVALLI DI 30 SECONDI ---
    
    # Intervallo temporale in secondi
    TIME_STEP = 30 
    
    # Otteniamo il timestamp Unix (secondi dall'epoch)
    # È cruciale che client e server abbiano l'ora sincronizzata
    timestamp = datetime.datetime.now().timestamp()
    
    # Calcoliamo il contatore (T): il numero di intervalli di 30s trascorsi
    contatore_t = int(timestamp // TIME_STEP)
    
    chiave = "SicurezzaInformatica"
    # La stringa da hashare è ora basata sulla chiave e sul contatore (T)
    contatore_t = str(contatore_t)[4:]
    stringa_da_hashare = chiave + contatore_t
    stringa_da_hashare_pulita = stringa_da_hashare.replace(" ", "")
    
    print(f"Stringa da hashare: {stringa_da_hashare_pulita}")
    
    oggetto_hash = hashlib.sha256(stringa_da_hashare_pulita.encode())
    esadecimale = str(oggetto_hash.hexdigest())
    print(f"Stringa Hashata: {esadecimale}")
    return esadecimale


def start_server():
    print("Avviato in modalità SERVER")
    
    # Genera l'OTP iniziale
    otp_server =  calcola_valore_numerico(generate_hash())
    print(f"OTP Server {datetime.datetime.now().strftime('%H:%M:%S')} --> \"{otp_server}\"")
    
    while True:
        now = datetime.datetime.now()
        current_second = now.second

        # LOGICA DI ATTESA PER INTERVALLI DI 30 SECONDI
        if current_second < 30:
            # Prossimo trigger a :30 secondi del minuto corrente
            prossimo_trigger = now.replace(second=30, microsecond=0)
        else:
            # Prossimo trigger a :00 secondi del minuto successivo
            prossimo_trigger = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
        
        # Attendi finché non arriva quel momento
        wait_seconds = (prossimo_trigger - now).total_seconds()
        time.sleep(wait_seconds)

        # Azione ogni 30 secondi
        otp_server = calcola_valore_numerico(generate_hash())
        print(f"OTP Server {datetime.datetime.now().strftime('%H:%M:%S')} --> \"{otp_server}\"")


def start_client():
    print("Avviato in modalità CLIENT")
    
    # Genera l'OTP iniziale
    otp_client = calcola_valore_numerico(generate_hash())
    print(f"OTP Client {datetime.datetime.now().strftime('%H:%M:%S')} --> \"{otp_client}\"")
    
    while True:
        now = datetime.datetime.now()
        current_second = now.second

        # LOGICA DI ATTESA PER INTERVALLI DI 30 SECONDI
        if current_second < 30:
            # Prossimo trigger a :30 secondi del minuto corrente
            prossimo_trigger = now.replace(second=30, microsecond=0)
        else:
            # Prossimo trigger a :00 secondi del minuto successivo
            prossimo_trigger = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
        
        # Attendi finché non arriva quel momento
        wait_seconds = (prossimo_trigger - now).total_seconds()
        time.sleep(wait_seconds)

        # Azione ogni 30 secondi
        otp_client = calcola_valore_numerico(generate_hash())
        print(f"OTP Client {datetime.datetime.now().strftime('%H:%M:%S')} --> \"{otp_client}\"")


def main():
    scelta = input("Vuoi avviare come 'client' o 'server'? ").strip().lower()

    
    match scelta:
        case "server":
            start_server()
        case "client":
            start_client()
        case _:
            print("Scelta non valida. Usa 'client' o 'server'.")


if __name__ == "__main__":
    main()