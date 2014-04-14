#!usr/bin/env Python


# attribution: http://en.wikipedia.org/wiki/Insertion_sort

def insert_sort(ul):
    for i in range(1, len(ul)):
        num, index = ul[i], i
        while index > 0 and ul[index - 1] > num:
            ul[index] = ul[index - 1]
            index -= 1
        ul[index] = num
    return ul

if __name__ == '__main__':
    print "Calculating..."
    from timeit import timeit

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
