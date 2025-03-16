
def trova_num_max(list_num):
    list_num.sort()
    n_max = list_num[-1]
    return n_max


my_list = [2, 6 ,89, 65, 4]

risultato = trova_num_max(my_list)
print(str(risultato))
