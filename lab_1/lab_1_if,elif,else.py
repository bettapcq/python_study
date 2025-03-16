#IF,ELIF,ELSE

#ESERCIZIO 1---------------------------------------------------------------

#score = 4

#if score >= 90:
#            print ("your grade is: A")
#elif score >= 80 and score <= 90:
#            print ("your grade is: B")
#elif score >= 70 and score <= 80:
#            print ("your grade is: C")
#elif score >= 60 and score <= 70:
#            print ("your grade is: D")
#else:
#            print ("your grade is: F")



#ESERCIZIO 2---------------------------------------------------------------

#year = 2024


#if year % 4 == 0:
#         if (year % 100 > 0) or (year % 100 == 0 and year % 400 == 0):
#                print(str(year) + " is a leap year")
#         else:
#            print(str(year) + " is not a leap year")

#else:
#            print(str(year) + " is not a leap year")





#ESERCIZIO 3---------------------------------------------------------------

#pwd = input("Scegli una password: ")
#numbers = set("1234567890")
#special = set("!@#$%^&*()")
#has_special_characters = any(c in special for c in set(pwd))
#has_numbers = any(c in numbers for c in set(pwd))
#forbidden_word = "password"

#if len(pwd) < 8:
#    print("La password è debole: deve contenere almeno 8 caratteri")
#elif forbidden_word in pwd.lower():
#    print("La password è debole: non deve contenere la parola _password_")
#elif (not has_numbers) and (not has_special_characters) :
#    print("La password è debole: inserisci almeno un numero e un carattere speciale")
#else:
#    print("La password è forte!")
