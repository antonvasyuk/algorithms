def bubble_sort(A):
    ''' сортировка пузырьком '''
    for i in range(1, len(A)):
        for j in range(len(A) - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A
