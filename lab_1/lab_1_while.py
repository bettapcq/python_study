
#CICLO WHILE, FUNZIONI BREAK,CONTINUE,FOR,RANGE

#ESERCIZIO 4

#item_name = ""
#item_quantity = 0
#item_price = 0

#item_price = float(item_price)
#item_quantity = float(item_quantity)
somma_items = 0
somma_price = 0


stop_number = 10
total_price = somma_items * somma_price
is_finished = False
stop_word = "finito"


while is_finished == False:
    item_name = input("inserisci il nome del prodotto: ")
    if item_name == stop_word:
        print("Ok, proseguiamo con il checkout." )
        break
    else:
        item_quantity = input("inserisci la quantità acquistata: ")
        somma_items += float(item_quantity)
        if item_quantity > 11:
            print("il carrello è pieno")
        else:
            item_price = input("inserisci il prezzo unitario: ")
            somma_price += float(somma_item)
            print("Ok, proseguiamo..")
            continue


print("La somma del tuo carrello è di " + total_price)
