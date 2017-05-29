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

## Disclaimer
Don't trust anything I say.

<sub><sup>1</sup>My feelings toward BSTs:</sub>

![image that encapsulates my feelings](http://tsnaomi.net/images/bst.png)

--------

### Doubly-linked list

 This repo implements the [*doubly-linked list*](https://en.wikipedia.org/wiki/Doubly_linked_list) data structure. A doubly-linked list is a sequence of nodes, wherein each node *links to* the previous and following node. This implementation includes the following methods:
  - `insert(val)` inserts *val* at the beginning of the list
  - `append(val)` appends *val* to the end of the list
  - `shift()` removes and returns the first value in the list
  - `pop()` removes and returns the last value in the list 
  - `remove(val)` removes the first instance of *val* in the list
  - `size()` returns the number of the nodes in the list (i.e., the list's length)
  - `contains(val)` returns True if the list contains *val*; otherwise, False
 
 These methods perform accordingly, where *n* is the number of nodes in a list:

 <!-- What is the space complexity analysis? O(n) or O(n^2)? -->
 ||insert|append|shift|pop|remove|size|contains|
 |---|---|---|---|---|---|---|---|
 |**Average**/**Worst**|O(1)|O(1)|O(1)|O(1)|O(*n*)|O(*n*)|O(*n*)|
 
 ([back to top](#data-structures))
   
### Queue

 A [*queue*](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) is a first-in-first-out or *FIFO* data structure, from which items are removed (*dequeued*) in the order that they were inserted (*enqueued*). This repo's implementation includes the following methods:
  - `enqueue(val)` appends *val* to the end of the queue
  - `dequeue()` removes and returns the first value in the queue
  - `peek()` returns the first value in the queue without removing it from the queue
  - `size()` returns the number of items in the queue

 <!-- What is the space complexity analysis? O(n) or O(n^2)? -->
 ||enqueue|dequeue|peek|size|
 |---|---|---|---|---|
 |**Average**/**Worst**|O(1)|O(1)|O(1)|O(1)|
 
 ([back to top](#data-structures))
  
### Stack

 A [*stack*](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) is a last-in-first-out or *LIFO* data structure, from which the most recently inserted items are removed first. This repo's implementation includes the following methods:
  - `push(val)` adds *val* to the top of the stack
  - `pop()` removes and returns the topmost (i.e., most recently added) value in the stack
  - `peek()` returns the first value in the stack without removing it from the stack
  - `size()` returns the number of items in the stack
  
 <!-- What is the space complexity analysis? O(n) or O(n^2)? -->
 ||push|pop|peek|size|
 |---|---|---|---|---|
 |**Average**/**Worst**|O(1)|O(1)|O(1)|O(1)|
 
 ([back to top](#data-structures))

### Binary heap

 <!-- A [*binary heap*](https://en.wikipedia.org/wiki/Binary_heap)... -->
 *[Binary heap](https://en.wikipedia.org/wiki/Binary_heap) description coming soon!*
 
 This repo's implementation of a binary heap includes the following methods:  
  - `push(val)` adds *val* to the heap, filling in the heap at the lowest level from left to right
  - `pop()` removes and returns the topmost value in the heap
  - `peek()` returns the topmost value in the heap without removing it from the heap
  - `size()` returns the number of items in the heap
 
 ||push|pop|peek|size|
 |---|---|---|---|---|
 |**Average**|O(1)|O(log *n*)|O(1)|O(1)|
 |**Worst**|O(log *n*)|O(log *n*)|O(1)|O(1)|

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
 -->

 ([back to top](#data-structures))

### Hash table

 *[Hash table](https://en.wikipedia.org/wiki/Hash_table) description coming soon!*
 
 This repo's implementation of a hash table includes the following methods:  
  - `set(key, val)` stores the *key*-*value* pair in the hash table (assuming that *key* is not already in the table)
  - `get(key)` retrieves the value stored at *key*
  
 ||set|get|
 |---|---|---|
 |**Average**|O(1)|O(1)
 |**Worst**|O(*n*)|O(*n*)|

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

 The *best* case for insertion sort is an input that is already sorted. With a sorted list, the algorithm merely iterates across the list without shifting any items, thus taking **O(*n*)** time, where *n* is the number of items in the list.

 The *worst* case is an input sorted in descending order. This forces the algorithm to shift the current value to the front of the sorted sub-list at each iteration, taking **O(*n*<sup>2</sup>)** time.

 The *average* case also takes **O(*n*<sup>2</sup>)** time, rendering it impractical for larger lists.

 |Best|Average|Worst|
 |---|---|---|
 |O(*n*)|O(*n*<sup>2</sup>)|O(*n*<sup>2</sup>)|
 
 ([back to top](#data-structures))

### Merge sort

 [*Merge sort*](https://en.wikipedia.org/wiki/Merge_sort) is a divide-and-conquer sorting algorithm. The implementation in this repo takes a *top-down* approach that recursively divides the input list into halves, sorts each halve, then merges the sorted halves back together.

 Merge sort always takes **O(*n* log *n*)** time, since the order of the input does not impact how often the algorithm invokes itself. See [here](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/analysis-of-merge-sort) for a more in-depth analysis of merge sort's performance.

 |Best|Average|Worst|
 |---|---|---|
 |O(*n* log *n*)|O(*n* log *n*)|O(*n* log *n*)|
 
 ([back to top](#data-structures))

### Quicksort

 [*Quicksort*](https://en.wikipedia.org/wiki/Quicksort) is another divide-and-conquer sorting algorithm. It picks a value, called a *pivot*, then *partitions* the input list into two sub-lists: a list containing values less than (or equal) to the pivot and a list containing values greater than the pivot. It then recursively sorts each sub-list accordingly. This repo implements both the [*Lomuto*](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme) and [*Hoare*](https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme) partitioning schemes.

 The *best* case for quicksort is a balanced input, where each partitioning results in two approximately equally-sized sub-lists. With such an input, quicksort takes **O(*n* log *n*)** time.

 Likewise, the *average* case for quicksort also takes **O(*n* log *n*)** time.

 The *worst* case for quicksort is when the partitioning results in an empty sub-list and a sub-list of size *n* - 1, taking **O(*n*<sup>2</sup>)** time to sort. This can happen if the pivot is equal to the lowest or greatest value in the input or, in the Lomuto scheme, when all of the items are equal in value. 

 |Best|Average|Worst|
 |---|---|---|
 |O(*n* log *n*)|O(*n* log *n*)|O(*n*<sup>2</sup>)|

 ([back to top](#data-structures))

### Radix sort

 *Coming (not so) soon!* Until then, check out this brief [YouTube video](https://www.youtube.com/watch?v=nu4gDuFabIM) on radix sort.

 ([back to top](#data-structures))
