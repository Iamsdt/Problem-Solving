# Problem statement
# Given a value V, if we want to make a change for V cents,
# and we have an infinite supply of each of C = { C1, C2, .., Cm}
# valued coins, what is the minimum number of coins to make the change?

# Lets solve with greedy algorithm

# Simple Explanation:
# 1. sort all the possible coins
# 2. if current note is less than value then reduce it
# otherwise move to next node

# problem with greedy, describe below

def coins(n, notes: list):
    notes.sort(reverse=True)
    p = 0
    di = {}
    while p < len(notes) and n != 0:
        value = notes[p]
        if n < value:
            p += 1
            continue

        n -= value
        if value in di:
            di[value] += 1
        else:
            di[value] = 1

    return di


if __name__ == "__main__":
    print(coins(504, [5, 10, 20, 30, 50, 100, 200, 500, 1000]))

#############################################################
##############################################################
"""
greedy algo always look for local optimum value
instead of global optimal value
for example
if n is 11 and notes -> 9, 5, 6, 1
solution will be -> 9, 1, 1
which is not current -> correct solution should be 5 and 6
To solve this we can use dynamic programming
"""
#############################################################
##############################################################