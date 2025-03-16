nums = [10, 9, 2, 5, 7, 13, 1, 101, 18, 1, 2, 4, 5, 6, 7, 9, 10, 11]

def find_longest_increasing_seq(lista):
    longest_list = []

    for idx in range(0, len(lista)):

        nuova_lista = [lista[idx]]

        for idx_2 in range(idx + 1, len(lista)):

            y = lista[idx_2 - 1]
            z = lista[idx_2]

            if y < z:
                nuova_lista.append(z)

            else:
                break

        if len(nuova_lista) > len(longest_list):
            longest_list = nuova_lista

    return longest_list



result = find_longest_increasing_seq(nums)
print (result)