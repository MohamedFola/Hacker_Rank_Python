def average(array):
    # write the code here
    setNumber = set(array)
    s = sum(setNumber)
    a = s / len(setNumber)
    return round(a, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
