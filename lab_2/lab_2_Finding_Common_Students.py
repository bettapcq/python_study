math_students = ["Alice", "Bob", "Charlie", "David"]
science_students = ["Charlie", "David", "Eve", "Frank"]

def finding_common_students(math, science):
    both = []
    only_math = []
    only_science = []

    for idx in math:

        if idx in science:
                both.append(idx)
        else:
            only_math.append(idx)

    for idx_2 in science:

        if idx_2 not in math:
           only_science.append(idx_2)

    not_both = only_math + only_science

    return both, only_math, not_both

result = finding_common_students(math_students, science_students)
print(result)