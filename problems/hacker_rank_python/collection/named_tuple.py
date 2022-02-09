from collections import namedtuple
n = int(input())

Score = namedtuple('Score',"MARKS ID NAME CLASS".split())

print(Score(*input().split()).MARKS)

# scores = [Score(*input().split()).MARKS for i in range(n)]

# print("%.2f"% (sum(map(int,scores))/n))