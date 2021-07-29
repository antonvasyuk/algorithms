def counting_sort(A):
    ''' сортировка подсчётом '''
    c = [0] * (max(A) + 1)
    for i in range(len(A)):
        c[A[i]] += 1
    j = 0
    for i in range(len(c)):
        for _ in range(c[i]):
            A[j] = i
            j += 1
    return A
