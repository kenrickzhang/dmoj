threshold = int(input())
infectees = int(input())
infectious = int(input())

days_elapsed = 0
total_infectees = infectees

while total_infectees <= threshold:
    infectees *= infectious
    total_infectees += infectees
    days_elapsed += 1

print(days_elapsed)