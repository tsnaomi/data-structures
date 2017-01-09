def insertion_sort(L):
    '''Sort list 'L' using Insertion Sort.'''
    for i, val in enumerate(L):
        j = i - 1

        while j >= 0 and L[j] > val:
            L[j + 1] = L[j]
            j -= 1

        L[j + 1] = val

    return L
