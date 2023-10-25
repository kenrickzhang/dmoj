# inputs
N = int(input())
board_lengths = input().split()

# convert list elements to int - easier to calculate
for i in board_lengths:
    i = int(i)

sums_list = []
for x in board_lengths:
    for y in board_lengths:
        if x != y:
            sums = int(x) + int(y)
            sums_list.append(sums)

common_sum = max(sums_list, key=sums_list.count)
common_sums_list = []

for x in board_lengths:
    for y in board_lengths:
        if int(x) + int(y) == common_sum:
            common_sums_list.append([x, y])

yes = True
while yes:
    for x in range(0, len(common_sums_list) - 1):
        for y in range(0, len(common_sums_list) - 1):
            if x > len(common_sums_list) - 1 or y > len(common_sums_list) - 1 :
                break

            if int(common_sums_list[x][0]) + int(common_sums_list[x][1]) == int(common_sums_list[y][0]) + int(common_sums_list[y][1]):
                common_sums_list.pop(y)
                break
            break
    
    common_sum = max(common_sums_list, key=common_sums_list.count)
    if common_sums_list.count(common_sum) == 1:
        yes = False

print(len(common_sums_list), max(common_sums_list[0]))