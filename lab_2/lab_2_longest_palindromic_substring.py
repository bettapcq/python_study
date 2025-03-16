w = ["a", "n", "n", "r", "c", "b", "a", "b", "c", "s", "n", "a", "n"]

def longest_palindromic_substring(word):

    longest_pal = []
    length = len(word)

    for idx in range(0, length):
        new_list = [word[idx]]

        for idx_2 in range(idx - 1, idx + 1):
            if word[idx] == word[idx_2]:
                new_list.append(idx)
                new_list.append(idx_2)
            else:
                break

        if len(new_list) > len(longest_pal):
            longest_pal = new_list
    return longest_pal

result = longest_palindromic_substring(w)
print(result)







#    while idx >= 0 and idx_2 < len(word) and word[idx] == word[idx_2]:
#        idx -= 1
#        idx_2 += 1
