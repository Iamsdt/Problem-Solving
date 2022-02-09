
times = int(input())

for _ in range(times):
    row, col = map(int, input().split())

    table = []
    # now take rows of table
    for _ in range(row):
        table.append(input())

    results = []

    # we are going one by one
    for i in range(row):
        top, bottom, topMax, bottomMax = 0, 0

        # if there is only one row
        if row == 1:
            results.append(table[i].count("#"))
            break

        # if multiple
        # then checking column wise
        for jj in range(col):

            # for first row
            # check it's black cell or not
            if i == 0 and table[i][jj] == "#":
                top += 1
                if table[i+1][jj] == ".":
                    bottom = bottom+1
                elif bottomMax < bottom: 
                    bottomMax = bottom
                    bottom=0

            elif i == 0 and jj == col - 1:
                if bottomMax<bottom: bottomMax=bottom 
                results.append(max([top, bottomMax]))

            # for last row
            if i == row - 1 and table[i][jj]=="#": 
                bottom=bottom+1
                if table[i-1][jj] ==".": 
                    top=top+1
                elif topMax<top:
                    topMax=top
                    top=0

            elif i==row-1 and jj==col-1:
                if topMax<top: topMax=top
                results.append(max([topMax, bottom]))

            # for middle only
            if i != 0 and i != row-1 and table[i][jj]=="#":
                if table[i-1][jj]==".": 
                    top=top+1
                elif topMax<top:
                    topMax=top
                    top=0
                if table[i+1][jj]==".": 
                    bottom=bottom+1
                elif bottomMax<bottom: 
                    bottomMax=bottom
                    bottom=0

            elif i!=0 and i!=row-1 and jj==col-1:
                if topMax<top: topMax=top       
                if bottomMax<bottom: bottomMax=bottom 
                results.append(max([topMax, bottomMax]))
    

    print(max(results))