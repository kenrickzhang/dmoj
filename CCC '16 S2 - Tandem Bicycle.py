question = int(input())
pairs = int(input())
dmojistan = input().split()
pegland = input().split()

for i in range(0, len(dmojistan)):
    dmojistan[i] = int(dmojistan[i])

for i in range(0, len(pegland)):
    pegland[i] = int(pegland[i])

# minimum total speed out of pair assignments
if question == 1:
    bicycle_list = []
    
    while len(dmojistan):
        
        max = 0
        max2 = 0

        for x in range(0, len(dmojistan)):
            if dmojistan[x] >= max:
                max = dmojistan[x]
                max_index = x
        
        dmojistan.pop(max_index)
                
        for y in range(0, len(pegland)):
            if pegland[y] >= max2:
                max2 = pegland[y]
                max_index2 = y

        pegland.pop(max_index2)
        
        bicycle_list.append([max, max2])
    
    total = 0
    for x in range(0, len(bicycle_list)):
        if bicycle_list[x][0] > bicycle_list[x][1]:
            total += bicycle_list[x][0]
        else:
            total += bicycle_list[x][1]
    print(total)

else:
    bicycle_list = []
    
    while len(dmojistan):
        
        max = 0
        min = 1000000

        for x in range(0, len(dmojistan)):
            if dmojistan[x] >= max:
                max = dmojistan[x]
                max_index = x
        
        dmojistan.pop(max_index)
                
        for y in range(0, len(pegland)):
            if pegland[y] <= min:
                min = pegland[y]
                min_index = y

        pegland.pop(min_index)
        
        bicycle_list.append([max, min])
    
    total = 0
    for x in range(0, len(bicycle_list)):
        if bicycle_list[x][0] > bicycle_list[x][1]:
            total += bicycle_list[x][0]
        else:
            total += bicycle_list[x][1]
    print(total)

# maximum total speed out of pair assignments
