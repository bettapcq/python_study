

word_list = []


while True:
    new_word = str(input("scegli una parola: "))

    if new_word in word_list:
        print("not ok")
        break
    else:
        word_list.append(str(new_word))
        print("ok")