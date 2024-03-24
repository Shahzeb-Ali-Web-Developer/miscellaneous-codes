t, p = map(int, input().split())
max, min = 0, 0
ans = 0
for i in range(t):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if i == 0:
        max = a
        min = b
    elif a > max:
        max = a
    elif b < min:
        min = b

    x = abs(max-p)
    y = abs(min-p)

    if max > min:       # when there is no overlapping segment
        ans = -1
    elif p >= max and p <= min:     # when position is already within track segment
        ans = 0
    else:                           # worst case, when basit will have to move
        if x > y:                   # checking k basit kis side k zyada kreeb h, start wali ya track k end wli
            ans = y
        else:
            ans = x

print(ans)