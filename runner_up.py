if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ar = list(arr)
    ar.sort()
    max = ar.pop(len(ar) - 1)
    for i in range(len(ar)):
        if not(ar[i] == max):
            runner = ar[i]
    for i in range(len(ar)):
        if not(ar[i] == max):
            if ar[i] >= runner:
                runner = ar[i]
    print(runner)
