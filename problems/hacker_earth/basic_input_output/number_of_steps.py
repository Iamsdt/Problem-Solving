length = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

mina = min(a)

ia = a.index(mina)

corb = b[ia]

steps = 0


def eval(num, target, substractor):

    step=0

    if num ==target:
        status = 1

    else:
        temp = num - target
        sta = temp%substractor
        if sta==0:
            status=1
            step = temp//substractor
        else:
            status = 0
            step = 0
    return (status, step)


 

while mina >= 0:

    for k in range(length):
        status, step = eval(a[k], mina, b[k])
        if status != 0:
            steps = step+steps
        else:
            steps = 0
            break
    if status ==1:
        break
    else:
        if corb == 0:
            break
        mina -= corb

if status==0:

    steps=-1

print(steps)