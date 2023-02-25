# Enter your code here. Read input from STDIN. Print output to STDOUT
i = int(input())
ls = set()
for _ in range(i):
    ls.add(input())

print(len(ls))
