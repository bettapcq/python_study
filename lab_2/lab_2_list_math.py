list_a = []
list_b = []
number = 0


def list_above_below_100(number, above, below):
    if number >= 100:
        above.append(number)
    else:
        below.append(number)

import random

for x in range(0, 300):
    random_number = random.randint(1, 300)
    list_above_below_100(random_number, list_a, list_b)

print(list_a, list_b)


def average_of_list(lista):
    list_sum = sum(lista)
    list_n = len(lista)
    list_average = list_sum / list_n
    return list_average


average = average_of_list(list_b)

print(average)

def remove_numbers(lista, number):
    lista_filtrata = []
    for n in lista:
        if n <= number - 10 or n >= number + 10:
            lista_filtrata.append(n)
    return lista_filtrata


nuova_lista = remove_numbers(list_a, 90)

print(nuova_lista)
