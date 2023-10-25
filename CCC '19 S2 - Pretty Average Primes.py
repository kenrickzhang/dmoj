count = int(input())
input_list = []
prime_sums = []

def is_prime(integer):
    if integer % 2 == 0 or integer in [0, 1]:
        return False
    
    for i in range(2, integer):
        if integer % i == 0:
            return False
        
    return True

for i in range(0, count):
    inp = int(input())
    input_list.append(inp)

for x in input_list:
    if is_prime(x):
        prime_sums.append([x, x])
    else:
        primes_found = False
        lesser, greater = x, x
        while not primes_found:
            lesser -= 1
            greater += 1
                
            if (lesser + greater) / 2 == x:
                if is_prime(lesser) and is_prime(greater):
                    prime_sums.append([lesser, greater])
                    primes_found = True
                
for i in prime_sums:
    print(i[0], i[1])