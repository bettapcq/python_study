

def find_palindrome (word):
    if word == word[::-1]:
        return "si palindromo"
    else:
        print("no palindrome")


def find_palindrome_2 (word):
    length = len(word)
    for idx in range(0, len(word) / 2):
        idx_2 = length - idx

        if word[idx] != word[idx_2]:
            return "no palindromo"

    return "si pal"


def find_palindrome_3 (word):
    length = len(word) / 2

    is_pal = True

    for idx in range(0, length):
        idx_2 = length - idx

        if word[idx] != word[idx_2]:
            is_pal = False
            break

    return is_pal


w = ["a", "n", "n", "r", "c", "b", "a"]

palindrome = find_palindrome(w)

print(palindrome)