#!usr/bin/env Python

# TODO: rename arguments, clean if-name-equals-main


def insert_sort(ul):
    for i in range(1, len(ul)):
        num, index = ul[i], i
        while index > 0 and ul[index - 1] > num:
            ul[index] = ul[index - 1]
            index -= 1
        ul[index] = num
    return ul


def merge_sort(ul):

    def merge(left, right):
        l = []
        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    l.append(left[0])
                    left = left[1:]
                else:
                    l.append(right[0])
                    right = right[1:]
            elif len(left) > 0:
                # l.append(left[0])
                # left = left[1:]
                l.extend(left)
                left = []
            else:
                # l.append(right[0])
                # right = right[1:]
                l.extend(right)
                right = []
        return l

    if len(ul) > 1:
        mid = len(ul) // 2
        left = merge_sort(ul[:mid])
        right = merge_sort(ul[mid:])
        ul = merge(left, right)
    return ul


if __name__ == '__main__':
    # from random import shuffle
    from timeit import timeit

    print 'Calculating'

    best = timeit('insert_sort([i for i in range(1, 1001)])',
                  setup='from __main__ import insert_sort', number=100)
    worst = timeit('insert_sort([i for i in range(1, 1001)[::-1]])',
                   setup='from __main__ import insert_sort', number=100)

    best, worst = best / 100, worst / 100

    print '''
        \n\tIt takes this insert_sort() method approximately \033[1m%s\033[0m
        seconds to 'sort' a \033[1mpre-sorted\033[0m list of numbers from 1 to
        1000 -- the best case input for an implementation of insertion sort.
        \n\tIn contrast, it takes approximately \033[1m%s\033[0m seconds for
        it to sort a \033[1mreverse\033[0m list of the same set of numbers --
        the worst case input for such an algorithm.
        \n\t'Twas about \033[1m%s\033[0m%% faster with the pre-sorted list.
        ''' % (best, worst, round(((worst - best) / worst) * 100, 2))

    print 'Calculating...'
    asc = [i for i in range(1, 1001)]
    desc = asc[::-1]
    a1, a2, inter = list(asc[:501]), list(asc[501:]), []
    while a2 and a1:
        inter.append(a2.pop())
        inter.append(a1.pop())
    # desc, shuf = asc[::-1], list(asc)
    # shuffle(shuf)

    asc = timeit('merge_sort(asc)',
                 setup='from __main__ import merge_sort, asc', number=100)
    desc = timeit('merge_sort(desc)',
                  setup='from __main__ import merge_sort, desc', number=100)
    # shuf = timeit('merge_sort(shuf)',
    #               setup='from __main__ import merge_sort, shuf', number=100)
    inter = timeit('merge_sort(inter)',
                   setup='from __main__ import merge_sort, inter', number=100)

    # asc, desc, shuf = asc / 100, desc / 100, shuf / 100
    asc, desc, shuf = asc / 100, desc / 100, inter / 100

    print inter

# print '''
#     \n\tAn implementation of merge_sort() has a best-, worst-, average-case
#     performance of O(n log n). Thus, calling merge_sort() on a pre-sorted
#     set of numbers will perform roughly the same as calling it on a list of
#     the same set of numbers sorted in reverse order or shuffled. (This
#     renders merge_sort() rather inefficient at 'sorting' pre-sorted lists.)
#     \n\tE.g., it takes this merge_sort() method approximately \033[1m%s
#     \033[0mseconds to sort a pre-sorted list of numbers from 1 to 1000,
#     \033[1m%s\033[0m seconds to sort the same list provided in reverse
#     order, and \033[1m%s\033[0m seconds to sort a shuffled version of the
#     same list.
#     \n\tAll in all, their performances did not a exceed a difference of
#     \033[1m%s\033[0m seconds.
#     ''' % (asc, desc, shuf, max(asc, desc, shuf) - min(asc, desc, shuf))

    print '''
        \n\tAn implementation of merge_sort() has a best case performance of
        O(n log n), as demonstrated by calling it on a list of numbers sorted
        in either ascending or descending order.
        \n\tIn contrast, calling this implementation of merge_sort() on an
        interwoven list of the same set of numbers will result in its worst
        case performance.
        \n\tIt takes this merge_sort() method approximately \033[1m%s
        \033[0mseconds to sort a pre-sorted list of numbers from 1 to 1000,
        \033[1m%s\033[0m seconds to sort the same list provided in descending
        order, and \033[1m%s\033[0m seconds to sort the interwoven version of
        the same set of numbers (e.g, 501, 1, 502, 2,...).
        \n\tHere, the best case performance is about \033[1m%s\033[0m%% faster
        than its worst case.
        ''' % (asc, desc, inter, round(
        ((inter - ((asc + desc) / 2)) / inter) * 100, 2))
