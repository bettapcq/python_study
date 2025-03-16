text = ""
error_message_empty = "la frase è vuota"
error_message_1_word = "La frase ha una sola parola. Devono essere almeno due"


def frequency_counter(frase):

    if not frase:
        raise Exception(error_message_empty) # trovo un problema, e creato un eccezione con un testo che voglio

    lista = frase.split()
    # vogliamo che se la lista ha solo una parola.
    if len(lista) == 1:
        raise Exception(error_message_1_word)
    count = {}

    for idx in range (0, len(lista)):
        parola = lista[idx]
        count.setdefault(parola, 0)
        if parola in count:
            count[parola] += 1

    return count

# miglioriamo ancora questo esempio
try:

    counter = frequency_counter(text)
    print(counter)
except Exception as my_ex: # gestisco l eccezione (che chiamo my_ex)
    # qua scegliamo cosa fare dell eccezione che abbiamo creato sopra.
    # in questo caso decidiamo di stampare un testo + .args
    # (in args sono salvate le cose che abbiamo scritto dentro le Execption()
    error_message = my_ex.args[0]
    # qua potremmo scegliere se gestire diversamente l errore. EG
    print("my first exception text is: ", error_message) # Con "except Exception as my_ex" abbiamo catturato la Exception lanciata
    if error_message == error_message_empty:
        print("la tua frase e' vuota. devi mettere una frase piu lunga")
    elif error_message == error_message_1_word:
        print("la tua frase e' troppo corta, ha una sola parola. Mettine almeno due")
    else:
        print("errore sconosciuto. qualcosa di strano e' successo")

    # spiegazione:
        # nella nostra funzione abbiamo trovato degli errori, in base a degli errori abbiamo creato Exception diverse (raise)
        # qua abbiamo gestito l errore. In base all errore avvenuto,abbiamo dato all utente un messagio diverso.
finally:
    print("qeusto codice e' sempre eseguito, anche se il programma ha errori")



# uso:
# in genere nel codice raise, try/except sono usati entrambi
# raise quando voglio dire che qualcosa nn va
# try catch quando voglio avere la gestione di qualcocsa che e' andato male

# raise example
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")
# questo si usa quando tu che scrivi il codice,
# vuoi mettere dei controlli di sicurezza (e.g la frase e' vuota). quando il controllo fallisce, allora raise un errore


# try/execpt example
#try:
#    print(x)
#except:
#    print("An exception occurred")
# questo si usa quando qualcun altro ha lanciato (raise) un errore
# il try chiama la funczione, l except viene eseguito se quella funzione lancia un errore. nell except possiamo decidere cosa fare con quell errore