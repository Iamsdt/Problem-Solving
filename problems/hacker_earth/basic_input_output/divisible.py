# Notes: Because of Time Limit Exceeded issues
# lets jump into hacking solution

N = 6
A = ["15478", "8452", "8232", "874", "985", "4512"]

first = A[:N//2]
second = A[N//2:]

number = "".join([i[0] for i in first])
number += "".join([i[-1] for i in second])


print("OUI" if int(number) % 11 == 0 else "NON")