new_word = "a"
last_word = "b"

while True:
    new_word = input("inserisci una parola: ")
    if new_word == last_word:
        print("la parola inserita è doppia!")
        break
    else:
        last_word = new_word