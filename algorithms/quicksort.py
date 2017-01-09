def hoare_quicksort(L, lo=None, hi=None):
    '''Sort list 'L' using Quicksort with Hoare partitioning.'''
    try:
        if int(lo) < hi:
            p = hoare_partition(L, lo, hi)
            hoare_quicksort(L, lo, p)
            hoare_quicksort(L, p + 1, hi)

    except TypeError:
        lo = 0
        hi = len(L) - 1
        hoare_quicksort(L, lo, hi)

    return L


def hoare_partition(L, lo, hi):
    '''Partition list 'L' using Hoare scheme.'''
    pivot = L[lo]
    i = lo - 1
    j = hi + 1

    while True:
        i += 1  # ?
        while L[i] < pivot:
            i += 1

        j -= 1  # ?
        while L[j] > pivot:
            j -= 1

        if i >= j:
            return j

        L[i], L[j] = L[j], L[i]


def lumoto_quicksort(L, lo=None, hi=None, hoare=True):
    '''Sort list 'L' using Quicksort with Lumoto partitioning.'''
    try:
        if int(lo) < hi:
            p = lumoto_partition(L, lo, hi)
            lumoto_quicksort(L, lo, p - 1)
            lumoto_quicksort(L, p + 1, hi)

    except TypeError:
        lo = 0
        hi = len(L) - 1
        lumoto_quicksort(L, lo, hi)

    return L


def lumoto_partition(L, lo, hi):
    '''Partition list 'L' using Lumoto scheme.'''
    pivot = L[hi]
    i = lo

    for j in range(lo, hi):
        if L[j] <= pivot:
            L[i], L[j] = L[j], L[i]
            i += 1

    L[i], L[hi] = L[hi], L[i]

    return i
