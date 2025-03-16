from math import exp, sqrt

command = 0
end_number = -1

while command >= 0:
    command = int(input("scegli l'operazione: "))
    if command == 1:
        a = int(input("numero 1: "))
        b = int(input("numero 2: "))
        somma = a + b
        print(somma)
    elif command == 2:
        a = int(input("numero 1: "))
        b = int(input("numero 2: "))
        sottrazione = a - b
        print(sottrazione)
    elif command == 3:
        a = int(input("numero 1: "))
        b = int(input("numero 2: "))
        moltiplicazione = a * b
        print(moltiplicazione)
    elif command == 4:
        a = int(input("numero 1: "))
        b = int(input("numero 2: "))
        divisione = a / b
        print(divisione)
    elif command == 5:
        a = int(input("numero 1: "))
        b = int(input("numero 2: "))
        c_espon = exp(a,b)
        print(c_espon)
    elif command == 6:
        a = int(input("numero: "))
        r_q = sqrt(a)
        print(sottrazione)


