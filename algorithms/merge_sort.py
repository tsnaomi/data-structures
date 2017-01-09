# coding='utf-8'


def merge_sort(L):
    '''Sort list 'L' using Merge Sort.'''
    length = len(L)

    if length > 1:
        mid = length // 2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        L = merge(left, right)

    return L


def merge(left, right):
    '''Merge 'left' and 'right' lists.'''
    L = []

    while left and right:

        if left[0] <= right[0]:
            L.append(left[0])
            left = left[1:]

        else:
            L.append(right[0])
            right = right[1:]

    L.extend(left)
    L.extend(right)

    return L
