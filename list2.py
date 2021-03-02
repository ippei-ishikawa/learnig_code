H = int(input())

# N <= 10**12

a = [0, 1, 1]
b = [0, 1, 1]

dmg = 2

i = 2

while dmg < H:
    a[0] = a[1]
    a[1] = a[2]
    b[0] = b[1]
    b[1] = b[2]

    a[2] = b[0] + b[1]
    b[2] = a[0] + 2 * a[1]

    dmg += b[2]

    i += 1

print(i)