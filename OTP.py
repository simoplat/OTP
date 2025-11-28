import hashlib
import datetime as TIME


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
        
        # 2. Limitiamo l'operazione ai primi 3 caratteri (come richiesto)
        if iterazione == 10:
            break 
    risultato_stringa = risultato_stringa[:tronca]
    return int(risultato_stringa)



orario_corrente = TIME.datetime.now().strftime("%Y-%m-%d %H:%M")
chiave = "Sicurezza"
stringa_da_hashare = chiave + orario_corrente
stringa_da_hashare_pulita = stringa_da_hashare.replace(" ", "")
print(f"Stringa da hashare: {stringa_da_hashare_pulita}")

# I dati devono essere codificati in byte (.encode())
oggetto_hash = hashlib.sha256(stringa_da_hashare_pulita.encode())

# Ottenere l'hash in formato esadecimale
esadecimale = oggetto_hash.hexdigest()



print(f"Hash SHA256: {esadecimale}")
print(f"Valore numerico totale dei caratteri della stringa: {calcola_valore_numerico(esadecimale)}")




