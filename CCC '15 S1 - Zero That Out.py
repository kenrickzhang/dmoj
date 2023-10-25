count = int(input())
number_list = []

for i in range(0, count):
    number_input = int(input())
    number_list.append(number_input)

i = 0
while 0 in number_list:
    i = number_list.index(0)
    
    if number_list[i] == 0:
        number_list.pop(i)
        number_list.pop(i - 1)

total_sum = 0
if number_list:
    for i in number_list:
        total_sum += i
print(total_sum)