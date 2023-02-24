if __name__ == '__main__':
    s = input()
    b = [False, False, False, False, False]

    for i in range(len(s)):
        if s[i].isalnum():
            b[0] = True

        if s[i].isalpha():
            b[1] = True

        if s[i].isdigit():
            b[2] = True

        if s[i].islower():
            b[3] = True

        if s[i].isupper():
            b[4] = True

for i in b:
    print(i)
