a = 60
b = 20
def calcGCD(a, b):
    min_factor = min(a, b)
    if min_factor == 1:
        return 1
    elif a % min_factor == 0 and b % min_factor == 0:
        return min_factor
    else:
        min_factor -= 1
        calcGCD(a, b)

print("GDC is: ",calcGCD(a, b))