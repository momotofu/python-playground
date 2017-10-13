n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

def fastPairWise(list = []):
    maxIndexOne = -1;
    maxIndexTwo = -1;

    # find greatest max index 1
    for i in range(0, n):
        if maxIndexOne == -1 or list[i] > list[maxIndexOne]:
            maxIndexOne = i

    for j in range(0, n):
        if list[j] != list[maxIndexOne] and (maxIndexTwo == -1 or list[j] > list[maxIndexTwo]):
            maxIndexTwo = j
    return list[maxIndexOne] * list[maxIndexTwo]

def slowPairWise(list = []):
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result

print('fast result: ', fastPairWise(a), 'slow result: ', slowPairWise(a))

