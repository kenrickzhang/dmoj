# get square
rows = []
for i in range(4):
    row_input = input()
    rows.append(row_input)
# check rows
magic = True
check_rows = 0
check_cols = 0
for i in rows[0].split():
    check_rows+=int(i)
for i in rows:
    row_sum = 0
    for x in i.split():
        row_sum += int(x)
    if row_sum != check_rows:
        magic = False
        break
# check columns
for i in rows:
    check_cols += int(i.split()[0])
for i in rows:
    column_sum = 0
    for x in range(4):
        column_sum += int(i.split()[x])
    if column_sum != check_cols:
        magic = False
        break

if magic:
    print("magic")
else:
    print("not magic")