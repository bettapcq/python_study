
students_grades = {"Alice" : [70, 60], "Bob" : [60, 65]}

def add_grade(dizionario, chiave, valore):

    if "chiave" in dizionario:

        dizionario[chiave].append(valore)

    return dizionario

update_alice = add_grade(students_grades, students_grades["Alice"], 75)
print(update_alice)

update_bob = add_grade(students_grades, students_grades["Bob"], 80)
print(update_bob)