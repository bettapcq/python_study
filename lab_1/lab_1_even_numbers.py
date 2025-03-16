def crea_lista(n_list):
    even_list = filter(lambda number: number % 2 == 0, n_list)
    return even_list


risultato = crea_lista([3, 5, 8, 7])
print(list(risultato))


risultato = crea_lista([3, 1, 3,77])
print(list(risultato))


risultato = crea_lista([1, -1, 3, 5])
print(list(risultato))
