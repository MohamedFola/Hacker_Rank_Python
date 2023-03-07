def print_formatted(number):
    length = len(bin(number)) - 2
    for i in range(1, number+1):
        d = str(i).rjust(length)
        o = str(oct(i))[2:].rjust(length)
        h = str(hex(i))[2:].rjust(length).upper()
        b = str(bin(i))[2:].rjust(length)
        print(d, o, h, b)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
