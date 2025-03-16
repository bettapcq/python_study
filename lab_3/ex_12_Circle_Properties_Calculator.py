
import math #perchè rimane grigio? -> perche nn lo hai usato.
# in pycharm se dichiari cose e nn le usi si lamenta e le mette grigie

radii = [1, 2, 3, -6]

# if a number is negative throw an exception and print the error message that is put inside the exception -- quale numero? quello della lista giusto?
def circle_prop_calcul(lista):

    for raggio in lista:

        if raggio < 0: # quando conviene fare questo check?
            raise Exception("errore, il numero è negativo")

        dict_raggio = {}
        # quando hai il raise di un exception, il flusso del programma cambia.
        # se c'e un errore anziche andare alla linea successiva, esce dal programma e va dove trova la prima try/except
        # se non c'e un errore invece continua alla linea succesiva
        # quindi in questo caso else e' inutile perche sappiamo gia che se e' positivo, il programma ha continuato
        # e allora il raggio e' sicuramente > 0
        # e' allineato con l if, perche il flusso e':
        # if regola fallita allora raise errore
        # altrimenti linea successiva faccio quello che devo fare -- ok capito

        area = raggio * raggio * math.pi
        circonferenza = raggio * math.pi * 2

        dict_raggio["area"] = area
        dict_raggio["circonf"] = circonferenza

        # TODO aggiungere il risultato a un lista risultati # eg: [{"area", 2, "circ", 3}, .....] -- ok -- ok






