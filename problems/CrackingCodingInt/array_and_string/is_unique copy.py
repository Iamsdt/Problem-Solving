# String And Array Problems
# *****************************************
# Problem: Write an algrothim to check
# in a string that all the characters are
# unique and what if you can not use any
#  additional data structure
# *****************************************

# Input
# HI -> True

def is_unique(string: str) -> bool:
    if len(string) > 128:
        return False

    li = [False for i in range(128)]
    for i in string:
        value = ord(i)
        # print(value)

        if (li[value]):
            return False

        li[value] = True

    return True


def check(string: str) -> bool:
    # Brute Force technique
    for i in range(len(string)-1):
        for j in range(i + 1, len(string)-1):
            if(string[i] == string[j]):
                return False

    return True

# using sorting algo
def uniqueCharacters(st):
    # Using sorting
    sorted(st)
 
    for i in range(len(st)-1):
        # if at any time, 2 adjacent
        # elements become equal,
        # return false
        if (st[i] == st[i + 1]) :
            return False
    
    return True

if __name__ == "__main__":
    print(is_unique("helo"))
    print(check("helo"))
    print(uniqueCharacters("helo"))
