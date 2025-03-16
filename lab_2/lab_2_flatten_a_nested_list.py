nested = [[2, 4, 6], [1, 3, 5], [10, 200, 300], [65]]

def flatten_list(nested_list):
    flat = []
    for n in nested_list:
        for y in n:
            flat.append(y)
    return flat

my_flatten_list = flatten_list(nested)

print(my_flatten_list)