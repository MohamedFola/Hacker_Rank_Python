# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    ls = map(int, input().split())
    t = tuple(ls)
    print(hash(t))
