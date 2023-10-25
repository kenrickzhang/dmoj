lower_input = int(input())
higher_input = int(input())

total_RSA = 0

for i in range(lower_input, higher_input + 1):
    divisors = 0
    
    for x in range(1, i + 1):
        if i % x == 0:
            divisors += 1
    
    if divisors == 4:
        total_RSA += 1

print(f"The number of RSA numbers between {lower_input} and {higher_input} is {total_RSA}")