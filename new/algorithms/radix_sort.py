# coding='utf-8'


def radix_sort(L):
    '''Sort list 'L' using Radix Sort.'''
    if L:
        digits = len(str(max(L)))

        for n in range(digits):
            bins = [[] for b in range(10)]

            for i in L:
                bins[i / (10 ** n) % 10].append(i)

            L = reduce(lambda x, y: x + y, bins)

    return L
