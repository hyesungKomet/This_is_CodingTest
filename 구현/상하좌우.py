x, y = 1, 1

N = int(input())
road = input().split()

for arrow in road:
    if arrow == 'R':
        if y != N:
            y += 1
    elif arrow == 'L':
        if y != 1:
            y -= 1
    elif arrow == 'U':
        if x != 1:
            x -= 1
    elif arrow == 'D':
        if x != N:
            x += 1

print(x, y)
