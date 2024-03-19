#Even Odd

num = int(input())
i = 1
if num % 2 == 0:
    while i <= num:
        print(f'{i}', end=" ")
        i = i + 1
else:
    while i <= num:
        print(f'{num}', end=" ")
        num = num - 1
