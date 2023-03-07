# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = [int(x) for x in input().split()]

p = int((N-1)/2)

for i in range(p):
    print((('.|.') * ((i*2)+1)).center(M, '-'))

print("WELCOME".center(M, '-'))

for i in range(p-1, -1, -1):
    print((('.|.') * ((i*2)+1)).center(M, '-'))
