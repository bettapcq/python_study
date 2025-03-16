#ES SUM1

#number_range = int(input("inserisci quantità di numeri da calcolare: "))
#total = 0

#for number in range(number_range):
#    print(number)
#    selected_number = int (input("inserisci il numero scelto: "))
#    total += selected_number

#average = selected_number / (number_range)

#print("Somma = " + str(total))
#print("media = " + str(average))


#ES SUM2

#number = True
#total = 0
#num_count = 0
#selected_number = 0
#skip = -999



#while number == True:
#    selected_number = int (input("inserisci il numero scelto: "))
#    if selected_number == skip:
#        print("il numero non è valido")
#       break
#    total += int(selected_number)
#    num_count += 1
#    average = total / num_count
#print("la somma dei numeri è: " + str(total))
#print("la media dei numeri è: " + str(average))





#ES SUM3

#number = True

#total_odd = 0
#total_even = 0
#even_count = 0
#odd_count = 0
#selected_number = 0
#skip = -999



#while number == True:
#    selected_number = int (input("inserisci il numero scelto: "))
#    if selected_number == skip:
#        print("il numero non è valido")
#        break
#    if selected_number % 2 == 0:
#        even_count += 1
#        total_even += int(selected_number)
#    else:
#        odd_count += 1
#        total_odd += int(selected_number)

#print("la somma dei numeri pari è: " + str(total_even))
#print("la somma dei numeri dispari è: " + str(total_odd))
#print("hai inserito " + str(even_count) + " numeri pari")
#print("hai inserito " + str(odd_count) + " numeri dispari")


#ES SUM4

#number = True
#selected_number = 0
#skip = 1000
#somma = 0
#counter = 0


#while number == True:
#    selected_number = int(input("inserisci il numero scelto: "))
#    counter += 1
#    somma += int(selected_number)
#    if somma >= skip:
#        print("stop loop")
#        break



#ES PIRAMID


total_n_line = 5


for n_line in range(1, total_n_line + 1):
    print("")
    for piramid in range(1, n_line + 1):

        print(piramid, end="")





for n_line in range(1, total_n_line + 1):
    print("")
    for piramid in range(total_n_line, n_line, - 1):

        print(piramid, end="")