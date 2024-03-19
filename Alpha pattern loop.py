#Alpha Pattern Loop

i = 1
num = int(input())
capstart = 65
smallend = 122
capital = num + capstart
small = smallend - num

while (i <= num) and (smallend >= small):
    print(chr(capstart), end=" ")
    print(chr(smallend), end=" ")
    capstart = capstart + 1
    i = i + 1 ; smallend = smallend - 1
