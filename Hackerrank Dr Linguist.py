s = str(input())

counts = []

uniques = []
for c in s:
    if c not in uniques:
        uniques.append(c)

for i in uniques:
    count = 0
    for j in s:
        if i == j:
            count += 1
    counts.append(count)

counts.sort()

counts[-1] = counts[-1]-1

ans = "YES"
for n in range(len(counts)-1):
    if counts[n] != counts[n+1]:
        ans = "NO"
        break

print(ans)