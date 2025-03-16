price_tot = 0
item = ""


for x in range(0, 10):
    item = input("inserisci il prodotto: ")
    if item == "done":
        break
    else:
        q = int(input("inserisci la quantità: "))
        p = float(input("inserisci il prezzo: "))
        price_tot += p * q
print(price_tot)