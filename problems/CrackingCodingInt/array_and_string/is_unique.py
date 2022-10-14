# String And Array Problems
# *****************************************
# Problem: Write an algrothim to check
# in a string that all the characters are
# unique and what if you can not use any
#  additional data structure
# *****************************************

# Input
# HI -> True
# Hello -> False

# Brute Force technique
def is_unique(st):

    # length
    if len(st) > 128:
        return False

    for i in range(len(st) - 1):  # o(n)
        for j in range(i + 1, len(st) - 1):  # o(n)
            if (st[i] == st[j]):  # o(1)
                return False

    return True


print(is_unique("HI"))
print(is_unique("Hello"))

# Complexity -> o(1) + o(n) * o (n) + o (1) -> o(n2)

# sorting algo
