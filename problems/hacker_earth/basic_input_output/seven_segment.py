n= int(input())
di = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

for i in range(n):
    digit = input()

    total_case = 0

    for jj in digit:
        total_case += di[int(jj)]

        
    one = total_case // 2

    if total_case % 2 == 0:
        print("1"*one)
    else:
        # why 7? it is the largest number with min value
        print("7"+"1"*(one-1))
