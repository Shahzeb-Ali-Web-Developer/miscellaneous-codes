#converts counting from one to hunred

num = int(input("Number : "))
a = num // 10
b = num % 10
if b == 1:
    b = "one"
elif b == 2:
    n = "two"
elif b == 3:
    n = "three"
elif b == 4:
    n = "four"
