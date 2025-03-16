numbers_list = [1, 3, 2, 5, 8, 4, 6]


def find_pairs_with_sum(lista, target):
    pairs_list = []
    for n in lista:
        for y in lista:
            if n + y == target:
                pairs_list.append((n, y))
    return pairs_list

def find_pairs_with_sum_improved(lista, target):
    pairs_list = []

    for dito in range(0, len(lista)):
        n = lista[dito]
        for dito_2 in range(dito, len(lista)):
            y = lista[dito_2]
            if n + y == target:
                pairs_list.append((n, y))

    return pairs_list


target_sum_pairs = find_pairs_with_sum_improved(numbers_list, 10)

print(target_sum_pairs)
