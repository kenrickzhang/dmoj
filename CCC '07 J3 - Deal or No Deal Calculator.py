number_left = int(input())
case_amounts = (100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000)
case_numbers = []

for i in range(0, number_left):
    case_input = int(input())
    case_numbers.append(case_input)

new_amounts = []
for i in range(0, 10):
    if i + 1 not in case_numbers:
        new_amounts.append(case_amounts[i])

total_sum = 0
for i in new_amounts:
    total_sum += i

total_sum_average = total_sum / len(new_amounts)

banker_offer = int(input())
if banker_offer > total_sum_average:
    print("deal")
else:
    print("no deal")