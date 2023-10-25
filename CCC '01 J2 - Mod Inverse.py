x = int(input())
m = int(input())
flag = False
modular = 0

for i in range(1, m):
    if (i * x) % m == 1:
        modular = i
        flag = True
        break

if flag:
    print(modular)
else:
    print("No such integer exists.")