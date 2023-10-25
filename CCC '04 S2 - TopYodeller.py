yodeller_count, rounds = input().split()
yodeller_count, rounds = int(yodeller_count), int(rounds)
round_list = []
# number: [points, lowestrank]
yodeller_dict = {}

# get string input split scores formatted
for i in range(0, rounds):
    temp_scores = input()
    round_list.append(temp_scores.split())

# convert to int
for x in range(0, rounds):
    for y in range(0, yodeller_count):
        round_list[x][y] = int(round_list[x][y])

# making the dict with first round values
for x in range(1, yodeller_count + 1):
    yodeller_dict[x] = [x, round_list[0][x-1], 0]

# rank them
sort_list = []
sort = False
for x in yodeller_dict:
    sort_list.append(yodeller_dict[x])
while not sort:
    for x in range(0, len(sort_list) - 1):
        if sort_list[x][1] > sort_list[x + 1][1]:
            print(f"{sort_list[x][1]} > {sort_list[x + 1][1]}")
            temp_y = sort_list[x + 1]
            sort_list[x + 1] = sort_list[x]
            sort_list[x] = temp_y
            continue
    sort = True

print(sort_list)