test_cases = int(input())
score_list = []
move_list = []
final_list = []

for i in range(0, test_cases):
    score = int(input())
    move = int(input())
    
    score_list.append(score)
    move_list.append(move)

for i in range(0, test_cases):
    current_score = score_list[i]
    current_move = move_list[i]
    
    min_score = current_score
    
    for i in range(0, current_move):
        for i in range(0, len(str(current_score)) - 1):
            current_score = int(str(current_score)[:i] + str(current_score)[i + 1:])
            print(current_score)
            if current_score < min_score:
                min_score = current_score
    
    final_list.append(min_score)

print(final_list)