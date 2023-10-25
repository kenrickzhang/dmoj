rounds = int(input())
rpsf_input = []
optimal = {"Rock":"Paper",
           "Paper":"Scissors",
           "Scissors":"Rock",
           "Fox":"Foxen"}

for i in range(0, rounds):
    temp_input = input()
    rpsf_input.append(temp_input)

for i in rpsf_input:
    if i == "Foxen":
        break
    print(optimal[i])