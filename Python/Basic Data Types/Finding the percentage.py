
# @turalmehrali
n = int(input())
arr = []
for i in range(n):
    name_score = []
    for j in input().split():
        name_score.append(j)
    arr.append(name_score)

name = input()
sum_score = 0
count = 0

for k in arr:
    if k[0] == name:
        for g in k[1:]:
            sum_score += float(g)
            count += 1

res = sum_score / count
print("{0:.2f}".format(res))

