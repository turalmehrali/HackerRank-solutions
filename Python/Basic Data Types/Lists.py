
commands = []
final_arr = []

for i in range(int(input())):
    command = []
    for j in input().split():
        command.append(j)
    commands.append(command)

for c in commands:
    if c[0] == 'insert':
        final_arr.insert(int(c[1]), int(c[2]))

    elif c[0] == 'print':
        print(final_arr)

    elif c[0] == 'remove':
        final_arr.remove(int(c[1]))

    elif c[0] == 'append':
        final_arr.append(int(c[1]))

    elif c[0] == 'sort':
        final_arr.sort()

    elif c[0] == 'pop':
        final_arr.pop(-1)

    elif c[0] == 'reverse':
        final_arr.reverse()

