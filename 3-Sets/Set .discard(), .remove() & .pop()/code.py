# the idea is to get the string and spilt it to two info
# first part is the command
# second part is the number to remove or discard

n = int(input())
s = set(map(int, input().split()))

iterator = int(input())

for i in range(iterator):
    a = list(input().split())
    if a[0] == "pop":
        s.pop()
    elif a[0] == "remove":
        s.remove(int(a[1]))
    elif a[0] == "discard":
        s.discard(int(a[1]))

print(sum(s))
