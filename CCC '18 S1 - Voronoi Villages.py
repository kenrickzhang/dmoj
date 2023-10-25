number_villages = int(input())
villages = []
sorted = False

for i in range(0, number_villages):
    n = int(input())
    villages.append(n)

villages.sort()
least_i = 1000000000

for i in range(1, len(villages) - 1):
    i_size = (villages[i] - villages[i-1]) / 2 + (villages[i+1] - villages[i]) / 2
    if i_size <= least_i:
        least_i = i_size

print(least_i)