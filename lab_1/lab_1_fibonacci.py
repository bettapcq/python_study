a = 0
b = 1
n = 50
f = 0

print(a)
print(b)


while f < n:
    f = a + b
    print(f)
    if f >= 1:
        a = b
        b = f
        f = a + b
    else:
        print("stop")