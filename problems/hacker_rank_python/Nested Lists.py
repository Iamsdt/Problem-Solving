if __name__ == '__main__':

    li = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        li.append([score, name])

    # remove max value
    m = min(li)
    a = [i for i in li if i[0] != m[0]]

    # this max is the second max
    m1 = min(a)
    final = [j for j in a if m1[0] == j[0]]
    # print
    print(*sorted([b[1] for b in final]), sep='\n')

