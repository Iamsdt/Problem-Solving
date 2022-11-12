n, k = 3, 2 # map(int, input().split())

arr = [3, -1, -2] #map(int, input().split()) #[3, -1, -2]

total = 0
counter = 0
m=k
flag=False

for i in arr:
    print(i)
    print(total, counter, m)
    if(i >= 0):
        counter += 1
        total += i
        m = k
        continue
    
    if(counter == 0):
        print(abs(sum(arr)+i))
        flag=True
        break
    else:
        m -= 1
        total += abs(i) if m < 0 else i
        

if flag==False:
    print(abs(total))