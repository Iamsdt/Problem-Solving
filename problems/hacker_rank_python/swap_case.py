def swap_case(s):
    n = ""

    for i in s:
        if i.islower():
            n += i.upper()
        elif i.isupper():
            n += i.lower()
        else:
            n += i

    return n


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
