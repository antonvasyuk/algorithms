def quick_sort(A):
    '''быстрая сортировка в функциональном стиле'''
    from random import random
        if len(A) <= 1:
            return A
        else:
            q = random.choise(A)
            L = [i for i in A if i < q]
            M = [q] * A.count(q)
            R = [i for i in A if i > q]
        return quick_sort(L) + M + quick_sort(R)
