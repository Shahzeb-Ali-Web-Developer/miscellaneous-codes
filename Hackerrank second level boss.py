length = int(input())
l = list(map(int, input().split()))
raw = []
for n in l:
    if n not in raw:
        raw.append(n)
new = sorted(raw)
if len(new) == 1:
    print("NO")
else:
    print(new[len(new) - 2])