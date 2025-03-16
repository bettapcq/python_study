#Il mio primo programma python




#ESERCIZIO 1

shop_name = "Betta"
meal1 = "lasagna"
meal2 = "maccheroni"
meal3 = "tiramisu"

print("Ciao, Benvenuto da " + shop_name + "!")

meal1_price = input("Inserisci per favore il prezzo del piatto " + str(meal1))
meal2_price = input("ora inserisci il prezzo di un piatto di " + str(meal2))
meal3_price = input("e quanto costa invece una porzione di " + str(meal3) + "?")

total_price = int(meal1_price) + int(meal2_price) + int(meal3_price)

medium_price = total_price / 3

shop_name = "Betta"
meal1 = "lasagna"
meal2 = "maccheroni"
meal3 = "tiramisu"


print("Ciao, Benvenuto da " + shop_name + "!")


meal1_price = input("Inserisci per favore il prezzo del piatto " + str(meal1))
meal2_price = input("ora inserisci il prezzo di un piatto di " + str(meal2)
meal3_price = input("e quanto costa invece una porzione di " + str(meal3) + "?")
meal1_quantity = input("Quante porzioni ordini di " + str(meal1) + "?")
meal2_quantity = input("Quante piatti ordini di " + str(meal2) + "?")
meal3_quantity = input("Quante porzioni ordini di " + str(meal3) + "?")

total_price_meal1 = int(meal1_price) * int(meal1_quantity)
total_price_meal2 = int(meal2_price) * int(meal2_quantity)
total_price_meal3 = int(meal3_price) * int (meal3_quantity)

total_amount = total_price_meal1 + total_price_meal2 + total_price_meal3

print("Il totale del ordine è:" + str(total_amount))

print("A presto")



