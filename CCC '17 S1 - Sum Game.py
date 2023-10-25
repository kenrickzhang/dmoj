N = int(input())
runs_scored_swifts = input().split()
runs_scored_semaphores = input().split()

score_swifts = 0
score_semaphores = 0
equality_max = 0

for i in range(0, N):
    score_swifts += int(runs_scored_swifts[i])
    score_semaphores += int(runs_scored_semaphores[i])
    
    if score_swifts == score_semaphores:
        equality_max = i + 1

print(equality_max)