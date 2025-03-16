N = 5
number = 0
prev_num = 0



for loop in range(1, N + 1):
    number = int(input("inserisci un numero: "))
    if number >= prev_num:
            prev_num = number
print("il numero max è: " + str(prev_num))