TOTAL_TAPE = 0

length = int(input())

row1 = input().split()
row2 = input().split()

for i in range(0, length):
    triangle = int(row1[i])

    # if black
    if triangle:
        # if even
        if i % 2 == 0:
            TOTAL_TAPE+=3

            if i > 0:
                if int(row1[i-1]) == 1:
                    TOTAL_TAPE-=1

            try:
                if int(row1[i+1]) == 1:
                    TOTAL_TAPE-=1
            except IndexError:
                TOTAL_TAPE = TOTAL_TAPE

            if int(row2[i]) == 1:
                TOTAL_TAPE-=1
        # if odd
        else:
            TOTAL_TAPE+=3

            if i > 0:
                if int(row1[i-1]) == 1:
                    TOTAL_TAPE-=1

            try:
                if int(row1[i+1]) == 1:
                    TOTAL_TAPE-=1
            except IndexError:
                TOTAL_TAPE = TOTAL_TAPE

for i in range(0, length):
    triangle = int(row2[i])

    # if black
    if triangle:
        # if even
        if i % 2 == 0:
            TOTAL_TAPE+=3

            if i > 0:
                if int(row2[i-1]) == 1 == 1:
                    TOTAL_TAPE-=1


            try:
                if int(row2[i+1]) == 1:
                    TOTAL_TAPE-=1
            except IndexError:
                TOTAL_TAPE = TOTAL_TAPE

            if int(row1[i]) == 1:
                TOTAL_TAPE-=1
        # if odd
        else:
            TOTAL_TAPE+=3

            if i > 0:
                if int(row2[i-1]) == 1:
                    TOTAL_TAPE-=1

            try:
                if int(row2[i+1]) == 1:
                    TOTAL_TAPE-=1
            except IndexError:
                TOTAL_TAPE = TOTAL_TAPE

print(TOTAL_TAPE)