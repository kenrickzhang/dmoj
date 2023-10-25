alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

keyword = input().upper()
word = input().upper()
indices_list = []
new_word = ""
final_phrase = ""

for i in word:
    if i in alphabet:
        new_word += i

index_length = len(keyword)

for i in range(0, index_length):
    new_list = []
    for x in range(i, len(new_word), index_length):
        new_list.append(new_word[x])
    indices_list.append(new_list)

for x in range(0, len(indices_list)):
    for y in range(0, len(indices_list[x])):
    
        indices_list[x][y] = alphabet[(alphabet.index(indices_list[x][y]) + alphabet.index(keyword[x])) % 26]

for x in range(0, len(indices_list) + 5):
    for y in range(0, len(indices_list)):
        try:
            final_phrase += indices_list[y][x]
        except:
            continue

print(final_phrase.strip())