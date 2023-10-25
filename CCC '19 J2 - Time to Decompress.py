lines = int(input())
line_list = []

for i in range(0, lines):
    line = input()
    line_list.append(line)

for i in range(0, len(line_list)):
    current_line = ""
    for x in range(0, int(line_list[i].split()[0])):
        current_line = current_line + line_list[i].split()[1]
    print(current_line)