# @turalmehrali

n = input()
shoes_numbers = [int(i) for i in input().split()]
count = int(input())
money = 0

for j in range(0, count):
    sh_num, cost = input().split()

    if int(sh_num) in shoes_numbers:
        money += int(cost)
        shoes_numbers.remove(int(sh_num))


print(money)
