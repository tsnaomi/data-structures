[![Build Status](https://travis-ci.org/tsnaomi/data-structures.png?branch=master)](https://travis-ci.org/tsnaomi/data-structures)

## Data Structures
- [Doubly-linked list](#doubly-linked-list)
- [Queue](#queue) (*something British*)
- [Stack](#stack) (*something having to do with pancakes*)
- [Binary heap](#binary-heap)
- [Hash table](#hash-table)
- [Graph](#graph) (**todo**: implement traversal and weighted edges)
- [Binary search tree](#binary-search-tree)<sup>1</sup> (**todo**: implement self-balancing)

## Algorithms
- [Insertion sort](#insertion-sort)
- [Merge sort](#merge-sort)
- [Quicksort](#quicksort)
- [Radix sort](#radix-sort)

<sub><sup>1</sup>My feelings toward BSTs:</sub>

![image that encapsulates my feelings](http://tsnaomi.net/images/bst.png)

--------

### Doubly-linked list

<!--
space... O(N)
size... O(1)
contains... O(N) / search
insert... O(1) 
append... O(N)
pop... O(1)
shift... O(N)
remove... O(N)
-->

<!-- ||Insert|Delete|Search|
|---|---|---|---|
|**Average**/**Worst**|O(1)|O(1)|O(*n*)| -->
  
  
### Queue

<!--
space... O(N)
enqueue... O(1)
dequeue... O(1)
peek... O(1)
size... O(1)

-->

<!-- ||Insert|Delete|Search|
|---|---|---|---|
|**Average**/**Worst**|O(1)|O(1)|O(*n*)| -->
  
  
### Stack

<!--
space... O(N)
push... O(1)
pop... O(1)
peek... O(1)
size... O(1)
-->

<!-- ||Insert|Delete|Search|
|---|---|---|---|
|**Average**/**Worst**|O(1)|O(1)|O(*n*)| -->

### Binary heap

<!-- - binary tree (if there are the right number of nodes, odd number)
- complete, except possibly the last level, balanced as possible; every non-terminal node has two children 
- filling in left to right, from the lowest level, so every heap with n nodes has the same shape
- any node is at least as large as its children
- heap property: a node is either >= (max) or <= (min) its children
- space... O(n)
- the height of the heap for n nodes i O(log n)
- find max... O(1)
- insertion... add to the bottom, swap with parent depending on the heap property, worst O(log n), average O(1)
- root deletion... worst O(log n), average O(1) 
- peek o(1) -->


### Hash table

<!-- 
space... O(n)
set... worst O(n), where n is the number of bins
get... worst O(n + m), # number of bins plus number of key-vales pairs

-->

<!-- ||Insert|Delete|Search|
|---|---|---|---|
|**Average**|O(1)|O(1)|O(1)|
|**Worst**|O(*n*)|O(*n*)|O(*n*)| -->

### Graph

<!--
undirect graph implementation, adjacency list

let N = # of nodes (V)
    E = # of edges (E)

space...
add node... O(1)
add edge... O(1)

del node... O(2E) == O(E)
del edge... O(N)

has node... O(N)
adjacent... O(E)  ? (assumes dict lookup is O(1))
neighbors... O(1) ? (assumes dict lookup is O(1))
-->

### Binary search tree

<!-- ||Insert|Delete|Search|
|---|---|---|---|
|**Average**|O(log *n*)|O(log *n*)|O(log *n*)|
|**Worst**|O(*n*)|O(*n*)|O(*n*)| -->

--------

### Insertion sort

[*Insertion sort*](https://en.wikipedia.org/wiki/Insertion_sort) constructs a sorted list one item at a time by iterating up the provided list and accruing a sorted sub-list behind it. At each position in the list, it compares the current value with the previous value. If the current value is greater, the algorithm moves on to the next iteration. Otherwise, it moves the current value to its correct position in the sub-list and shifts all rightward values in the sub-list up by one position.

The *best* case for insertion sort is an input that is already sorted, which takes **(O(*n*))** time, where *n* is the number of items in the list.

The *worst* case is an input sorted in reverse order. This forces the algorithm to shift the current value to the front of the sorted sub-list at each iteration, taking **O(*n*<sup>2</sup>)** time.

The *average* case also takes **O(*n*<sup>2</sup>)** time, rendering it impractical for larger lists.

|Best|Worst|Average|
|---|---|---|
|O(*n*)|O(*n*<sup>2</sup>)|O(*n*<sup>2</sup>)|

### Merge sort

<!-- |Best|Average|Worst|
|---|---|---|
|O(*n* log *n*)|O(*n* log *n*)|O(*n* log *n*)|
 -->

### Quicksort

<!-- |Best|Average|Worst|
|---|---|---|
|O(*n* log *n*)|O(*n* log *n*)|O(*n*<sup>2</sup>)|
 -->

### Radix sort
