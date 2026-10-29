a = [2, 3, 2]
m = [3, 5, 7]

M = 1

for i in m:
    M *= i

x = 0

for i in range(len(m)):
    mi = M // m[i]

    for j in range(1, m[i]):
        if (mi * j) % m[i] == 1:
            inv = j
            break

    x += a[i] * mi * inv

x = x % M

print("Solution x =", x)