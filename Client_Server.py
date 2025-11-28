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
        if iterazione == 10:
            break 
    risultato_stringa = risultato_stringa[:tronca]
    return int(risultato_stringa)


def generate_hash():
    orario_corrente = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    chiave = "SicurezzaInformatica"
    stringa_da_hashare = chiave + orario_corrente
    stringa_da_hashare_pulita = stringa_da_hashare.replace(" ", "")
    print(f"Stringa da hashare: {stringa_da_hashare_pulita}")
    oggetto_hash = hashlib.sha256(stringa_da_hashare_pulita.encode())
    esadecimale = oggetto_hash.hexdigest()
    return esadecimale


def start_server():
    print("Avviato in modalità SERVER")
    otp_server =  calcola_valore_numerico(generate_hash())
    print(f"OTP Server {datetime.datetime.now().strftime('%H:%M:%S')} --> \"{otp_server}\"")
    while True:
        now = datetime.datetime.now()
        
        # Calcola il prossimo minuto esatto (secondi = 0)
        prossimo_minuto = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
        # Attendi finché non arriva quel momento
        wait_seconds = (prossimo_minuto - now).total_seconds()
        time.sleep(wait_seconds)

        # Azione ogni minuto
        otp_server = calcola_valore_numerico(generate_hash())
        print(f"OTP Server {datetime.datetime.now().strftime('%H:%M:%S')} --> \"{otp_server}\"")


def start_client():
    print("Avviato in modalità CLIENT")
    otp_client = calcola_valore_numerico(generate_hash())
    print(f"OTP Server {datetime.datetime.now().strftime('%H:%M:%S')} --> \"{otp_client}\"")
    while True:
        now = datetime.datetime.now()
        
        # Calcola il prossimo minuto esatto (secondi = 0)
        prossimo_minuto = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
        # Attendi finché non arriva quel momento
        wait_seconds = (prossimo_minuto - now).total_seconds()
        time.sleep(wait_seconds)

        # Azione ogni minuto
        otp_client = calcola_valore_numerico(generate_hash())
        print(f"OTP Server {datetime.datetime.now().strftime('%H:%M:%S')} --> \"{otp_client}\"")


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
