# Extracted from: bxab107.pdf
**Total Pages**: 11
**Extraction Date**: 2026-07-20

---

## Page 1

Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
© The British Computer Society 2021. All rights reserved.
For permissions, please e-mail: journals.permissions@oup.com
Advance Access publication on 2 August 2021
https://doi.org/10.1093/comjnl/bxab107
Parallel Divide-and-Conquer
Algorithms for Bubble Sort, Selection
Sort and Insertion Sort
Pramod Ganapathi* and Rezaul Chowdhury
State University of New York at Stony Brook, NY 11794, USA
∗Corresponding author: pramod.ganapathi@cs.stonybrook.edu
We present efficient parallel recursive divide-and-conquer algorithms for bubble sort, selection
sort, and insertion sort. Our algorithms have excellent data locality and are highly parallel. The
computational complexity of our insertion sort is O

nlog2 3
in contrast to O

n2
of standard
insertion sort.
Keywords: parallel divide-and-conquer; sorting algorithm; bubble sort; selection sort; insertion sort;
merge sort; quicksort
Received 2 September 2020; Revised 14 April 2021; Accepted 7 June 2021
Handling editor: Petra Berenbrink
1.
INTRODUCTION
Sorting is a computational process of rearranging a multiset of
items in non-descending or non-ascending order [1]. Sorting
is used in real-life scenarios. Smartphone contacts are sorted
based on names; students’ (resp. employees’ and patients’)
profiles are sorted based on student ID (resp. employee ID
and patient ID); flight (or bus or train) information is sorted
based on time of departure; and, finally, the importance given
to different jobs/people are sorted based on our priorities.
Sorting is one of the most fundamental problems in computer
science. Sorting is used as an intermediate step to solve several
computer science problems [1, 2] such as bringing all items
with the same identification together, matching items in two or
more files, searching for a specific value, testing if all elements
are unique, deleting duplicates, finding the kth most frequently
occurring element, finding set union/intersection, finding the
closest pair of points, finding a convex hull and so on. Even
if sorting was totally useless, it is an exceptionally interesting
problem that leads to several beautiful algorithms and analyses.
For all these reasons, sorting is a well-studied problem and has
a large literature.
Several algorithms have been discovered to sort an array of
size n. More than six decades of research has yielded over
a hundred algorithms to solve the sorting problem, many of
which are either minor or major variations of tens of standard
algorithms. Sorting algorithms can be classified based on a
wide variety of conditions such as computational complexity,
in-place or not-in-place, stable or unstable, recursive or non-
recursive, comparison based or not comparison based, deter-
ministic or probabilistic, internal memory or external memory,
serial or parallel [3, 4], shared memory or distributed memory,
adaptive [5] or non-adaptive and self-improving [6] or non-self-
improving.
Divide-and-conquer algorithms for bubble, selection and
insertion sorts. Bubble, selection and insertion sorts [7] are
some of the most elementary sorting algorithms that are widely
taught to the students of computer science in the lower-level
undergraduate courses on algorithms and/or data structures.
These algorithms are inefficient but popular majorly because
they are arguably simple, intuitive, easy to remember and easy
to program. Some of the fastest sorting algorithms such as
merge sort and quicksort are then introduced to teach the
power of the divide-and-conquer (D&C) algorithm design
technique.
D&C is a powerful algorithm design technique used to
solve a problem by dividing it into two or more subproblems,
solving them and combining their solutions to solve the orig-
inal problem. D&C algorithms have the following important
advantages. (i) They are sometimes efficient [7] in the sense that
they reduce the total number of computations. (ii) They often
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 2

2710
P. Ganapathi and R. Chowdhury
TABLE 1.. Work (T1), serial cache complexity (Q1) and span (T∞) of iterative and recursive D&C algorithms for
bubble sort, selection sort and insertion sort (the serial cache complexity is given for n =  (M), where M ≥B; all
notations used are described in Table 2).
Existing algorithm
Our D&C algorithm
Work
Serial cache
Span
Work
Serial cache
Span
Problem
(T1)
complexity (Q1)
(T∞)
(T1)
complexity (Q1)
(T∞)
Result
Bubble sort [7]


n2


n2
B



n2


n2
O

n2
BM

 (n)
Section 2
Selection sort [7]


n2


n2
B



n2


n2
O

n2
BM

 (n)
Section 3
Insertion sort [7]
O

n2
O

n2
B

O

n2
O

nlog2 3
O

nlog2 3
BMlog2 3−1

O (n)
Section 4
are cache efficient1 [8–11], cache oblivious2 [12] and cache
adaptive3 [13, 14].
There are several other benefits of using the D&C design
technique. (i) The complexities (e.g. time, space and communi-
cation) of D&C algorithms can be analyzed using recurrences
[15] as such algorithms are typically implemented recursively.
(ii) They can be parallelized easily [16] as the subproblems
are typically independent. (iii) There exist frameworks to auto-
matically or semi-automatically generate D&C algorithms for
certain classes of computational problems [10, 17–19]. (iv) The
D&C algorithms can be architecture independent4 [20].
So, a natural question to ask is:
In this paper, we answer the question above affirmatively by
designing cache-efficient parallel D&C algorithms for bubble
sort, selection sort and insertion sort. Table 1 shows perfor-
mance comparison of our algorithms with the existing algo-
rithms. All our algorithms incur asymptotically fewer cache
misses than those of their iterative counterparts because they
exploit temporal data locality5 . Our algorithms are also highly
1 Cache-efficient algorithms are those that make efficient use of caches by bringing in
as less data as possible and using them as much as possible before evicting them.
2 Cache-oblivious algorithms are those that do not need to know machine parameters
such as cache sizes, block sizes and the number of levels of memory. Such algorithms are
portable across machines with different cache parameters.
3 Cache-adaptive algorithms are those that can adapt well to computing systems in
which the available memory changes dynamically.
4 Architecture-independent algorithms are those that run on both shared-memory and
distributed-memory machines with almost no change to their core algorithmic structure.
5 An algorithm must have the following two features in order to make good use of
cache. (i) Spatial data locality: Whenever a cache block is brought into the cache, it
contains as much useful data as possible. (ii) Temporal data locality: Whenever a cache
parallel. Furthermore, our insertion sort performs O

nlog2 3
computations, i.e. polynomially better than that of standard
insertion sort. But, it is also true that asymptotically improved
bubble, selection and insertion sorts are no match to the world’s
fastest sorting algorithms. Nevertheless, the most important
usefulness of our algorithms is not performance but peda-
gogy. In addition, designing and analyzing such algorithms
is theoretically interesting. The presented algorithms serve as
good examples or exercises to teach the design and analysis of
parallel D&C algorithms.
A parallel comparison sorting algorithm is work optimal
if it performs  (n log n) computations. Some parallel D&C
sorting algorithms such as two-way merge sort [21], two-way
randomized quicksort [21], √n-way randomized sample sort
[21],
3√n-way funnelsort [12] and √n-way distribution sort
[12] are work optimal and the computational complexity for
randomized quicksort is whp6 . Sorting algorithms such as ours
are not work optimal.
There are similarities and differences between our sort-
ing algorithms and parallel merge sort and parallel random-
ized quicksort. Our bubble and selection sorts use algorithm-
specific Partition idea similar to that of quicksort. Likewise,
our insertion sort uses algorithm-specific Merge idea similar
to that of merge sort. Unlike merge sort and quicksort, our
algorithms are not computationally efficient. This is because of
the slow Partition and Merge functions that our algorithms
use, which call themselves four or three times, respectively. In
contrast, the Merge function of merge sort calls itself twice
[21]. Similarly, the Partition function of quicksort usually
uses the PrefixSum function [21] instead of calling Partition
recursively and the PrefixSum function can be considered as
a two-way D&C. Some more differences are as follows. The
Merge function in standard merge sort is not-in-place, whereas
the Merge function in our D&C insertion sort is in-place.
block is brought into the cache, as much useful work as possible is performed on this data
before removing the block from the cache.
6 An event E is said to occur with high probability (whp) if Probability(E) ≥1−α/nβ,
where α ≥1 and β > 0 are constants.
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 3

Parallel Divide-and-Conquer Sorting Algorithms
2711
Quicksort Partition works on an array and uses a randomized
pivot whereas the Partition function in our D&C bubble and
selection sorts works on two arrays and does not use a pivot.
Our Contributions. The major contributions of this paper are
as follows: (1) [Theory.] We present parallel recursive D&C
algorithms for bubble sort, selection sort and insertion sort.
We prove their correctness and analyze their complexities,
as shown in Table 1. Our insertion sort performs O

nlog2 3
computations, i.e. polynomially better than that of standard
iterative insertion sort. Our algorithms are cache efficient and
highly parallel. (2) [Practice.] We implement the parallelized
and optimized versions of our algorithms and compare them
with their standard iterative counterparts to achieve around 20×
to 1300× speedup, depending on the algorithm and the input
distribution.
Related Work. Variations of bubble sort [22, 23] exist such
as cocktail sort [1], where the direction of bubbling alternates
between left-to-right and right-to-left, and odd–even sort [24].
Selection sort variants include bingo sort [25], which scans
the remaining elements to find the greatest value and shifts all
elements with that value to their final locations.
Insertion sort variants include shell sort [26], where elements
separated by a distance are compared; binary insertion sort,
which uses binary search to find the exact location of the
new elements to be inserted; heap sort [27], where insertions
and searches are performed with a sophisticated data structure
called a heap; and library sort [28], where small number of
spaces are left unused to make gaps for the elements to be
inserted. Insertion sort is generally faster than selection sort,
which typically is faster than bubble sort.
The cache performance of sorting algorithms have been
studied by LaMarca and Ladner [29]. The lower bounds for data
transfers for external-memory sorting algorithms are given by
Aggarwal and Vitter [30].
Model of Computation. We analyze the performance of a
parallel algorithm on a shared-memory multicore machine in
the binary-forking model [31] using the work-span perfor-
mance metrics [32]. The total number of computations of a
parallel algorithm is called work and denoted by T1(n). It is
also the serial running time of the algorithm. The running
time of an algorithm on a machine with an infinite number of
processors is called span and denoted by T∞(n). The parallel
running time of an algorithm on p processors, denoted by Tp(n),
when scheduled by a greedy scheduler is given by Tp(n) =
O (T1(n)/p + T∞(n)). The parallelism of an algorithm is com-
puted by the ratio T1(n)/T∞(n).
We analyze the performance of an algorithm using the cache-
oblivious model (or ideal-cache model) [12]. We measure the
total number of cache misses or page faults, called cache
complexity. Cache complexity captures the total number of data
transfers between adjacent levels of memory. It is important
to reduce data movements because communication is usually
TABLE 2.. Notations used in paper.
Symbol
Meaning
A
Array to be sorted
n
Number of array elements
b
Base case size
ℓ, h, m
Low, high and mid
ℓℓ
Left subarray’s low index
rh
Right subarray’s high index
p
Number of processors
M, B
Cache size, cache line size
T1
Work or total #computations
T∞
Span or critical-path length
Tp
Parallel running time
T1/T∞
Parallelism
Q1
Serial cache complexity
Qp
Parallel cache complexity
more expensive than computation. The serial cache complexity,
denoted by Q1(n), is the cache complexity of an algorithm on a
serial machine. On the other hand, the parallel cache complex-
ity is Qp(n) = O (Q1(n) + p(M/B)T∞(n)) with high proba-
bility when run under the randomized work-stealing scheduler
on a p-processor parallel machine with private caches. Here, M
and B denote the cache size and the cache line size, respectively,
where M ≥B.
Organization of the Paper. The paper is organized as follows.
In Sections 2, 3 and 4, we present D&C algorithms for bubble
sort, selection sort and insertion sort, respectively. In Section 5,
we present experimental results of our algorithms. We conclude
in Section 6.
2.
BUBBLE SORT
Table 2 summarizes the notations used in the paper. The array
to be sorted is A[0..n −1]. For simplicity, we assume that n is
a power of 2. In all recursive function calls, we use notations
such as ℓ, h, m, ℓℓ, ℓh, rℓ, rh, etc., all of which represent indices
in array A. Notations ℓ, m and h mean low, mid and high,
respectively. Terms ℓℓand rm mean low in the left subarray
and mid in the right subarray, respectively. Other terms can be
defined in a similar way. When subproblem size (h −ℓ+ 1) or
say (ℓh −ℓℓ+ 1) becomes less than or equal to the base case
size b, then we execute an iterative base case kernel having an
algorithm-dependent logic.
A simple iterative algorithm BubbleSort-Iterative is
given in Figure 1. It has n iterations. In each iteration i
(∈[0, n −1)), every two adjacent elements j and j + 1, where
j ∈[0, n−i−1], are compared and sorted if they are not already
in their sorted order. The number of comparisons at iteration
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 4

2712
P. Ganapathi and R. Chowdhury
FIGURE 1.. A recursive D&C bubble sort algorithm: initial call to
the recursive algorithm is BubbleSort(A[0..n−1]), where A[0..n−1]
is the array to be sorted.
i is n −i and at the end of the iteration, the array’s (i + 1)th
largest element will be in its correct position.
A recursive D&C bubble sort algorithm BubbleSort is
shown in Figure 1. The aim is to sort the entire array A[0..n−1].
The function BubbleSort(A[ℓ..h]) sorts the subarray A[ℓ..h].
The initial invocation to the algorithm is BubbleSort(A[0..n−
1]). The function in turn calls the Partition function. The
Partition function brings the smallest n/2 elements to the
left half and the largest n/2 elements to the right half of
array A. Once the array A is partitioned, then BubbleSort is
recursively called onto the left and right halves in parallel to
sort the two halves. After the two halves are sorted recursively,
the entire array A[0..n −1] will be sorted. When a subproblem
reaches the base case, it is sorted using the standard iterative
bubble sort logic.
The partition function Partition(A[ℓℓ..ℓh], A[rℓ..rh]) par-
titions the elements such that after the partition, the largest
element in A[ℓℓ..ℓh] will be less than or equal to the smallest
element in A[rℓ..rh]. The function works as follows.
In the base case, we use two loops: the outer-loop ranging
over the right subarray and the inner-loop ranging over the left
subarray. Using a logic similar to that of iterative bubble sort,
the largest elements in the left subarray are pushed to the right
subarray after every iteration.
In the recursion case, the Partition calls itself four times.
The reason for requiring four function calls is simple. Let
ℓm and rm be the midpoints of the left and right subarray,
respectively. The left subarray A[ℓℓ..ℓh] can be divided into
two subarrays A[ℓℓ..ℓm] and A[(ℓm + 1)..ℓh] and the right
subarray A[rℓ..rh] can be divided into two subarrays A[rℓ..rm]
and A[(rm + 1)..rh]. This means there are a total of four
possible combinations of left and right subarrays. In the first
parallel step, the Partition function invokes two Partition
functions in parallel that work on different regions of the array.
In the second parallel step, two more Partition functions are
invoked in parallel that work on disjoint regions. After the four
self-invocations, the larger elements of the entire array would
have moved to the right subarray leaving the smaller elements
in the left subarray.
The proof of correctness and complexity analysis of
BubbleSort are given in Theorems 2.1 and 2.2, respectively.
Theorem 2.1. (Bubble Sort Correctness). BubbleSort
correctly sorts an unsorted array.
Proof. We use mathematical induction to prove the theorem.
First we prove the correctness of Partition function. Then we
prove BubbleSort correct. We assume that n and b are powers
of 2 such that n ≥b. We say A[ℓℓ..ℓh] and A[rℓ..rh] as left and
right input subarrays, respectively.
(1) [Correctness of Partition.] Basis. The base case logic
when the input subarray is of size b is straightforward. The
external loop runs b times and in each iteration, an element
that is greater than or equal to b number of elements moves to
the right subarray. Induction. We assume that Partition works
correctly when the input subarrays are of size 2k for some k,
such that 2k ≥b. We need to prove that Partition works for
subarrays of size 2k+1.
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 5

Parallel Divide-and-Conquer Sorting Algorithms
2713
Let Q1, Q2, Q3 and Q4, where Q stands for ‘quarter’, repre-
sent the subarrays A[ℓℓ..ℓm], A[(ℓm + 1)..ℓh], A[rℓ..rm], and
A[(rm + 1)..rh], respectively, where each subarray is of size
2k. Let W, X, Y, and Z be the initial sets (not lists) of numbers
present at Q1, Q2, Q3 and Q4, respectively. Let Small(S1, S2)
(resp. Large(S1, S2)) of two equal-sized sets S1 and S2 of
numbers represent a set consisting of the smallest half (resp.
largest half) of the numbers from sets S1 and S2. Also, let
S1 ≤S2 denote that all elements of S1 are less than or equal
to all elements of S2.
Consider the Partition function in Figure 1. After execu-
tion of line 9, the states of the four quarters of the array A are
Q1 = W, Q2 = X, Q3 = Y and Q4 = Z. After execution of line
10, the states of the four quarters of the array A are as follows:
Q1 = Small(W, Y), Q2 = Small(X, Z), Q3 = Large(W, Y)
and Q4 = Large(X, Z). After execution of line 11, the states
of the four quarters of the array A are
Q1 = Small(Small(W, Y), Large(X, Z))
Q2 = Small(Small(X, Z), Large(W, Y))
Q3 = Large(Small(X, Z), Large(W, Y))
Q4 = Large(Small(W, Y), Large(X, Z))
It is easy to see that
Q1 ≤Q4 and Q1 ≤Small(W, Y) ≤Large(W, Y) ≤Q3
Q2 ≤Q3 and Q2 ≤Small(X, Z) ≤Large(X, Z) ≤Q4
As Q1 ≤Q3, Q1 ≤Q4, Q2 ≤Q3 and Q2 ≤Q4, the input
subarrays of size 2k+1 have been partitioned.
(2) [Correctness of BubbleSort.] Basis. The base case when
the input subarray is of size b is exactly the same as the standard
iterative bubble sort.
Induction. We assume that BubbleSort works correctly when
the input subarrays are of size 2k for some k, such that 2k ≥b.
We need to prove that BubbleSort works for input subarrays
of size 2k+1. We know that the Partition function is correct
and hence after line 8, the left subarray (A[ℓ..m]) and the right
subarray (A[(m + 1)..h]) would be partitioned such that the
largest element in the left subarray will not be greater than the
smallest element in the right subarray. Then after line 9, we
recursively sort the subarrays without affecting the partition
constraint and hence the total subarray will be sorted.
■
Theorem 2.2. (Bubble Sort Complexity).
BubbleSort
incurs O(n2/(BM) + n/B + 1) cache misses and has  (n)
span.
Proof. Let Qf
1(n) and Tf
∞(n) denote the number of serial cache
misses and span of algorithm f, respectively. Let BS-I, BS,
and Part denote BubbleSort-Iterative, BubbleSort and
Partition, respectively. Then,
QBS-I
1
(n) = n−1
i=0  (((n −i)/B) + 1) = 

n2/B + n

.
QBS
1 (n) = QPart
1
(n) = O (n/B + 1)
if n ≤γ M,
QBS
1 (n) = 2QBS
1 (n/2) + QPart
1
(n/2) + O (1)
if n > γ M,
QPart
1
(n) = 4QPart
1
(n/2) + O (1)
if n > γ M.
TBS
∞(n) = TPart
∞
(n) = O (1)
if n = 1,
TBS
∞(n) = TBS
∞(n/2) + TPart
∞
(n/2) + O (1)
if n > 1,
TPart
∞
(n) = 2TPart
∞
(n/2) + O (1)
if n > 1,
where γ is a constant. The cache complexity of a subproblem
of size n when it fits cache, i.e. n ≤γ M, is  (n/B + 1) =
O (M/B + 1). The cache complexity of a subproblem when
it does not fit into cache is recursively computed using its
subproblems. The cache complexity recurrence can be solved
using an approach similar to the one given in the proof of
Theorem 4.2 and by replacing log 3 with log 4. The span
recurrence can be solved by using the master theorem [32, 33]
first on the Partition function and then on BubbleSort.
■
3.
SELECTION SORT
Selection sort is another slow running sorting algorithm that
sorts n numbers in O

n2
time.
An iterative algorithm SelectionSort-Iterative is given
in Figure 2. The algorithm has n iterations. In each iteration i
∈[0, n −1], the position of the minimum element, denoted
by min is found in the range A[i..n −1]. Then the elements
A[min] and A[i] are swapped. The algorithm makes sure that
after iteration i, the ith smallest element is in its correct position.
A recursive D&C selection sort algorithm SelectionSort
is shown in Figure 2. The initial invocation to the algorithm
is SelectionSort(A[0..n −1]). The recursive structure of
the algorithm is exactly the same as that of bubble sort. The
SelectionSort function invokes the Partition function to
partition the array A into two halves where the largest element
in the first half is lesser than or equal to the smallest element
in the second half. After the partition, the SelectionSort
functions are invoked on the two halves to sort them recursively.
The partition function Partition calls itself four times in
two parallel steps. The only difference between the bubble
sort and selection sort D&C algorithms are the base cases of
SelectionSort and Partition functions.
The base case kernel of SelectionSort function is equiva-
lent to SelectionSort-Iterative. In the base case kernel of
the Partition function, in each iteration, an element that is
lesser than or equal to b elements is pushed to the left subarray.
After several iterations, the elements in the two subarrays
would be partitioned in such a way that the largest element in
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 6

2714
P. Ganapathi and R. Chowdhury
FIGURE 2.. A recursive D&C selection sort algorithm: initial call
to the recursive algorithm is SelectionSort(A[0..n −1]), where
A[0..n −1] is the array to be sorted.
the left subarray A[ℓℓ..ℓh] would be lesser than or equal to the
smallest element in the right subarray A[rℓ..rh].
The proof of correctness and complexity analysis of
SelectionSort are given in Theorems 3.1 and 3.2, respec-
tively.
Theorem 3.1. (Selection Sort Correctness). Selection
Sort correctly sorts an unsorted array.
Proof. We use mathematical induction to prove the theorem.
First we prove the correctness of Partition function. Then we
prove SelectionSort correct. We assume that n and b are
powers of 2 such that n ≥b. We say A[ℓℓ..ℓh] and A[rℓ..rh]
as left and right input subarrays, respectively.
(1) [Correctness of Partition.] Basis. The logic of the base
case when the input subarray is of size b is straightforward. The
external loop runs b times. In each iteration, we find the index
of the smallest element in the right subarray and if that element
is less than an element in the left subarray, then we swap the
two elements. In this way, the smallest b elements will move
to the left subarray. Induction. The argument is similar to that
given in Theorem 2.2.
(2) [Correctness of SelectionSort.] Basis. The base case
when the subarray is of size b is exactly same as the standard
iterative selection sort. Induction. The argument is similar to
the one in Theorem 2.2.
■
Theorem 3.2. (Selection Sort Complexity). Selection
Sort incurs O(n2/(BM)+n/B+1) cache misses and has  (n)
span.
Proof. Let Qf
1(n) and Tf
∞(n) denote the number of serial cache
misses and span of algorithm f, respectively. Let SS-I, SS and
Part denote SelectionSort-Iterative, SelectionSort and
Partition, respectively. Then,
QSS-I
1
(n) = n−1
i=0  (((n −i)/B) + 1) = 

n2/B + n

.
QSS
1 (n) = QPart
1
(n) = O (n/B + 1)
if n ≤γ M,
QSS
1 (n) = 2QSS
1 (n/2) + QPart
1
(n/2) + O (1)
if n > γ M,
QPart
1
(n) = 4QPart
1
(n/2) + O (1)
if n > γ M.
TSS
∞(n) = TPart
∞
(n) = O (1)
if n = 1,
TSS
∞(n) = TSS
∞(n/2) + TPart
∞
(n/2) + O (1)
if n > 1,
TPart
∞
(n) = 2TPart
∞
(n/2) + O (1)
if n > 1,
where γ is a suitable constant. The cache complexity recur-
rence can be solved using an approach similar to the one
given in the proof of Theorem 4.2 and by replacing log 3 with
log 4. The span recurrence can be solved by using the master
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 7

Parallel Divide-and-Conquer Sorting Algorithms
2715
theorem [32, 33] first on the Partition function and then on
SelectionSort.
■
4.
INSERTION SORT
Insertion sort is a pretty fast algorithm compared with other
elementary sorting algorithms, which sorts a set of n elements
in O

n2
worst and average case time.
An iterative algorithm InsertionSort-Iterative is given
in Figure 3. The algorithm has n −1 iterations. In iteration i
∈[1, n −1), the array element A[i] will be inserted in a sorted
position in the range A[0..i −1]. After each iteration i, the
subarray A[0..i] will be sorted. The runtime complexity is data
sensitive.
A recursive D&C insertion sort algorithm InsertionSort
is shown in Figure 3. The initial invocation to the algorithm
is InsertionSort(A[0..n −1]). The recursive structure of the
algorithm is different from that of bubble and selection sorts.
The InsertionSort function calls itself twice to sort the left
and right halves separately and simultaneously. Then it invokes
the Merge function to merge the elements from the two halves
using the logic of the iterative insertion sort. After the merge,
the entire array would be sorted.
The merge function Merge calls itself a total of three
times: the first two calls in parallel and then a third serial
call. The first call Merge(A[ℓℓ..ℓm], A[rℓ..rm]) brings the
smallest elements to A[ℓℓ..ℓm] in sorted order. The second
call Merge(A[ℓm + 1..ℓh], A[rm + 1..rh]) brings the largest
elements to A[rm + 1..rh] in sorted order. The third call
Merge(A[ℓm + 1..ℓh], A[rℓ..rm])
brings
the
remaining
elements to A[ℓm + 1..rm] in the sorted order.
The base case kernel of InsertionSort function is equiva-
lent to InsertionSort-Iterative. The base case kernel of the
Merge function merges two sorted subarrays to a sorted array.
In iteration k, the kth element of the right subarray gets merged
with its previous elements in the right subarray and with the
elements of the left subarray. After rh −rℓ+ 1 iterations, the
elements in the two subarrays would be merged into a sorted
array—the left subarray will be sorted, the right subarray will
be sorted and the last element of the left subarray will be less
than or equal to the first element of the right subarray.
The proof of correctness and complexity analysis of
InsertionSort are given in Theorems 4.1 and 4.2, respec-
tively.
Theorem 4.1. (Insertion Sort Correctness). InsertionSort
correctly sorts an unsorted array.
Proof. We use mathematical induction to prove the theorem.
First we prove the correctness of the Merge function. Then
we prove InsertionSort correct. We assume that n and b are
powers of 2 such that n ≥b. We say A[ℓℓ..ℓh] and A[rℓ..rh] as
left and right input subarrays, respectively.
FIGURE 3.. A recursive D&C insertion sort algorithm: initial call to
the recursive algorithm is InsertionSort(A[0..n−1]), where A[0..n−
1] is the array to be sorted.
(1) [Correctness of Merge.] Basis. The logic of the base case
when the input subarray is of size b is straightforward. The
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 8

2716
P. Ganapathi and R. Chowdhury
external loop runs for all elements in the right subarray, i.e.
b times. In each iteration, the element from the right subarray
is inserted into its correct position towards its left by shifting
elements. Induction. We assume that Merge works correctly
when the input subarrays are of size 2k for some k, such that
2k ≥b. We need to prove that Merge works for input subarrays
of size 2k+1.
Let Q1, Q2, Q3, and Q4, where Q stands for ‘quarter’, rep-
resent the subarrays A[ℓℓ..ℓm], A[(ℓm + 1)..ℓh], A[rℓ..rm] and
A[(rm + 1)..rh], respectively, where each subarray is of size
2k. Let W, X, Y and Z be the initial sets (not lists) of numbers
present at Q1, Q2, Q3 and Q4, respectively. Let Small(S1, S2)
(resp. Large(S1, S2)) of two equal-sized sets S1 and S2 of
numbers represent a set consisting of the smallest half (resp.
largest half) of the numbers from sets S1 and S2. Also, let
S1 ≤S2 denote that all elements of S1 is less than or equal
to all elements of S2. As the input subarrays are sorted we
have W ≤X. Hence, we can write W = Small(W, X) and
X = Large(W, X). Similarly, Y ≤Z. Therefore, we can write
Y = Small(Y, Z) and Z = Large(Y, Z).
Consider the Merge function in Figure 3. After execution
of line 13, the states of the four quarters of the array A are
Q1 = W, Q2 = X, Q3 = Y and Q4 = Z. After execution
of line 14, the states of the four quarters of the array A are
Q1 = Small(W, Y), Q2 = Small(X, Z), Q3 = Large(W, Y),
and Q4 = Large(X, Z). After execution of line 15, the states
of the four quarters of the array A are
Q1 = Small(W, Y)
Q2 = Small(Small(X, Z), Large(W, Y))
Q3 = Large(Small(X, Z), Large(W, Y))
Q4 = Large(X, Z).
It is easy to see that
Q1 = Small(Small(W, X), Small(Y, Z))
= Small(Small(W, Y), Small(X, Z)) ≤Q2
Q2 ≤Q3
Q3 ≤Large(Large(X, Z), Large(W, Y))
= Large(Large(W, X), Large(Y, Z)) = Q4.
As Q1 ≤Q2 ≤Q3 ≤Q4, the input subarrays of size 2k+1
have been merged.
(2) [Correctness of InsertionSort.] Basis. The base case
when the input subarray is of size b is exactly same as the
standard iterative insertion sort. Induction. We assume that
InsertionSort works correctly when the input subarrays are
of size 2k for some k, such that 2k ≥b. We need to prove
that InsertionSort works for input subarrays of size 2k+1.
We know that the InsertionSort function is correct. Hence,
after line 11, the left subarray (A[ℓ..m]) would be sorted and the
right subarray (A[(m + 1)..h]) would be sorted. Then after line
12, we merge the two subarrays. As we have shown that the
merge function Merge is correct, the entire subarray of size
2k+1 would be merged and sorted.
■
Theorem 4.2. (Insertion Sort Complexity).
Insertion
Sort performs O

nlog2 3
work, incurs O(nlog2 3/(BM(log2 3)−1)+
n/B + 1) cache misses and has O (n) span.
Proof. Let Tf
1(n), Qf
1(n), and Tf
∞(n) denote the work, the num-
ber of serial cache misses and span of algorithm f, respectively.
Let IS-I, IS and Merge denote InsertionSort-Iterative,
InsertionSort and Merge, respectively. Then,
QIS-I
1
(n) = n−1
i=0 O (((n −i)/B) + 1) = O

n2/B + n

.
TIS
1 (n) = TMerge
1
(n) = O (1)
if n = 1,
TIS
1 (n) = 2TIS
1 (n/2) + TMerge
1
(n/2) +  (1)
if n > 1,
TMerge
1
(n) = 3TMerge
1
(n/2) +  (1)
if n > 1.
QIS
1 (n) = QMerge
1
(n) = O (n/B + 1)
if n ≤γ M,
QIS
1 (n) = 2QIS
1 (n/2) + QMerge
1
(n/2) + O (1)
if n > γ M,
QMerge
1
(n) = 3QMerge
1
(n/2) + O (1)
if n > γ M.
TIS
∞(n) = TMerge
∞
(n) = O (1)
if n = 1,
TIS
∞(n) = TIS
∞(n/2) + TMerge
∞
(n/2) + O (1)
if n > 1,
TMerge
∞
(n) = 2TMerge
∞
(n/2) + O (1)
if n > 1,
where γ is a suitable constant. The span recurrence can be
solved by using the master theorem [32, 33] first on the Merge
function and then on InsertionSort.
The derivation of the serial cache complexity of IS is given
as follows. We initially find QMerge
1
and then use it to compute
QIS
1 . We assume that n/2k = γ M for some γ and all logarithms
are taken to the base 2.
QMerge
1
(n) = 3QMerge
1
n
2

+  (1)
= 3kQMerge
1
 n
2k

+  (1)

3k−1 + · · · + 30
= 3k 
QMerge
1
 n
2k

+  (1)

= O
 n
M
log 3 M
B

= O

nlog 3
BMlog 3−1

Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 9

Parallel Divide-and-Conquer Sorting Algorithms
2717
FIGURE 4.. Speedup of the D&C bubble, selection and insertion sorts for (i) random input (left column) and (ii) descending order input (right
column) (the definition of speedup is given in Equation 1).
Plugging QMerge
1
into the recurrence of QIS
1 , we get
QIS
1 (n) = 2QIS
1
n
2

+ QMerge
1
n
2

+  (1)
= 2k 
QIS
1
 n
2k

+  (1)

+  (1) ·
 n
M
log 3 M
B

·
k
	
i=1

1
2(i−1)(log 3−1)

= O
 n
M
M
B

+
 n
M
log 3 M
B

= O

nlog 3
BMlog 3−1 + n
B + 1

Solving the recurrences we get the theorem.
■
5.
EXPERIMENTS
This section presents empirical results showing performance
improvements of the D&C sorting algorithms from high paral-
lelism and better cache complexity over their iterative counter-
parts.
Setup. Our experiments were performed on a multicore
machine with dual-socket 8-core 2.7 GHz Intel Sandy Bridge
processors (2 × 8 = 16 cores in total) and 32 GB RAM. Each
core was linked to a 32 KB private L1 cache and a 256 KB
private L2 cache. All cores in a processor shared a 20 MB
L3 cache. With hyper-threading, we can simulate a total of
32 threads from 16 cores. The algorithms were implemented
in C++. Intel Cilk Plus extension was used to parallelize
the programs. Intel C++ Compiler v13.0 (icc) was used
to compile the implementations with parameters -O3 -ipo
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 10

2718
P. Ganapathi and R. Chowdhury
-parallel -AVX -xhost. Apart from these parameters
no optimizations were used.
Implementations. The three standard iterative sorting algo-
rithms: BubbleSort-Iterative, SelectionSort-Iterative
and InsertionSort-Iterative were implemented without any
optimization and the implementations were inherently serial.
The D&C algorithms: BubbleSort, SelectionSort and
InsertionSort were also implemented without optimizations.
When the subproblem size (h −ℓ+ 1 or ℓh −ℓℓ+ 1) became
less than or equal to a base case size b = 28 = 256, we
switched to an iterative kernel having an algorithm-dependent
logic. The recursive algorithms were run with 32 threads. We
define speedup as follows:
Speedup =
Runtime of iterative algorithm
Runtime of recursive algo. with 32 threads
(1)
In our experiments, we used two types of input: (i) random
input (using rand function) and (ii) descending order input.
The input size n was varied from 28 = 256 to 219 = 524288
and the speedup was computed for different algorithms based
on Equation 1.
Results. Table 4 shows the speedup graphs for the three sorting
algorithms.
The speedup of the BubbleSort program increased from
0.7× to 76× for the random input when n increased. The super-
linear speedup is due to cache optimality. For the descending
order input, the speedup increased from 0.6× to 30.6×. The
good speedup is majorly due to parallelism and to some extent
by the cache performance.
The SelectionSort program speedup increased from ≈1×
to 23.9× for the random input when n increased. When the
input was in decreasing order, the speedup increased from ≈
1× to 19.8×. Compared to bubble sort, the speedup is less for
selection sort. The reason is that SelectionSort does more
number of comparisons than SelectionSort-Iterative.
For the random input, the speedup of the InsertionSort
program increased from 1.1× to 280×. For the decreasing
order input, the speedup increased from 1.1× to 1314.7×.
Note that such a large speedup is not possible from parallelism
and cache performance alone. The factor that is increasing the
speedup is the asymptotic less work that the InsertionSort
performs compared to InsertionSort-Iterative as shown in
Theorem 4.2.
6.
CONCLUSION
We presented parallel D&C algorithms for bubble sort, selec-
tion sort and insertion sort. The algorithms are fast (i.e. cache
efficient and parallel) and portable (i.e. cache oblivious). The
implementations of our algorithms run significantly faster than
their iterative counterparts. It would be interesting to know if
we can design parallel D&C algorithms related to more sorting
techniques.
DATA AVAILABILITY
No new input data were generated or analysed in support of this
research.
FUNDING
This work was supported in part by National Science Founda-
tion grants [CCF-1162196, CCF-1439084, CNS-1553510].
REFERENCES
[1] Knuth, D. E. (1998) The Art of Computer Programming: Sorting
and Searching. Pearson Education, Massachusetts.
[2] Skiena, S. S. (1998) The Algorithm Design Manual. Springer
Science and Business Media, London.
[3] Akl, S.G. (2014) Parallel Sorting Algorithms. Academic Press,
Florida.
[4] Cole, R. (1988) Parallel merge sort. SIAM J. Comput., 17,
770–785.
[5] Estivill-Castro, V. and Wood, D. (1992) A survey of adaptive
sorting algorithms. ACM Comput. Surv., 24, 441–476.
[6] Ailon, N., Chazelle, B., Clarkson, K.L., Liu, D., Mulzer, W.
and Seshadhri, C. (2011) Self-improving algorithms. SIAM J.
Comput., 40, 350–375.
[7] Levitin, A. (2011) Introduction to the Design and Analysis of
Algorithms (3rd edn). Pearson, New Jersey.
[8] Chatterjee, S., Lebeck, A.R., Patnala, P.K. and Thottethodi, M.
(2002) Recursive array layouts and fast matrix multiplication.
IEEE Trans. Parallel Distrib. Syst., 13, 1105–1123.
[9] Frens, J.D. and Wise, D.S. (1997) Auto-blocking Matrix-
Multiplication or Tracking BLAS3 Performance from Source
Code. In ACM Symposium on Principles and Practice of Parallel
Programming, vol. 32, pp. 206–216. ACM, Las Vegas, USA,
June 18–21.
[10] Chowdhury, R., Ganapathi, P., Tschudi, S., Tithi, J.J., Bachmeier,
C., Leiserson, C.E., Solar-Lezama, A., Kuszmaul, B.C. and Tang,
Y. (2017) Autogen: automatic discovery of efficient recursive
divide-&-conquer algorithms for solving dynamic programming
problems. ACM Trans. Parallel Comput., 4, 1–30.
[11] Chowdhury, R., Ganapathi, P., Pradhan, V., Tithi, J.J. and Xiao,
Y. (2016) An Efficient Cache-Oblivious Parallel Viterbi Algo-
rithm. In Proc. of the 22nd European Conf. on Parallel Process-
ing, pp. 574–587. Springer, Grenoble, France, August 22–26.
[12] Frigo, M., Leiserson, C.E., Prokop, H. and Ramachandran, S.
(2012) Cache-oblivious algorithms. ACM Trans. Algorithms, 8,
1–22.
[13] Bender, M.A., Ebrahimi, R., Fineman, J.T., Ghasemiesfeh, G.,
Johnson, R. and McCauley, S. (2014) Cache-Adaptive Algo-
rithms. In Proc. of the 25th ACM-SIAM Symposium on Discrete
Algorithms, pp. 958–971. SIAM ACM, Portland, USA, January
5–7.
[14] Bender, M.A., Demaine, E.D., Ebrahimi, R., Fineman, J.T.,
Johnson, R., Lincoln, A., Lynch, J. and McCauley, S. (2016)
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

## Page 11

Parallel Divide-and-Conquer Sorting Algorithms
2719
Cache-Adaptive Analysis. In Proc of the 28th ACM Symposium
on Parallelism in Algorithms and Architectures, pp. 135–144.
ACM, Pacific Grove, USA, July 11–13.
[15] Bentley, J.L. (1980) Multidimensional divide-and-conquer.
Commun. ACM, 23, 214–229.
[16] Mou, Z.G. and Hudak, P. (1988) An algebraic model for
divide-and-conquer and its parallelism. J. Supercomput., 2,
257–278.
[17] Chowdhury, R., Ganapathi, P., Tang, Y. and Tithi, J.J. (2017)
Provably Efficient Scheduling of Cache-Oblivious Wavefront
Algorithms. In Proc. of the 29th ACM Symposium on Parallelism
in Algorithms and Architectures, pp. 339–350. ACM, Washing-
ton DC, USA, July 24–26.
[18] Ganapathi, P. (2016) Automatic discovery of efficient divide-&-
conquer algorithms for dynamic programming problems. PhD
Thesis, Department of Computer Science. State University of
New York at Stony Brook.
[19] Ahmad, Z., Chowdhury, R., Das, R., Ganapathi, P., Gregory, A.
and Zhu, Y. (2021) Fast Stencil Computations Using Fast Fourier
Transforms. In Proc. of the 33rd ACM Symposium on Parallelism
in Algorithms and Architectures. ACM, Virtual Event, USA,
July 6–8.
[20] Javanmard, M.M., Ganapathi, P., Das, R., Ahmad, Z., Tschudi,
S. and Chowdhury, R. (2019) Toward Efficient Architecture-
Independent Algorithms for Dynamic Programs. In Int. Conf.
on High Performance Computing, pp. 143–164. Springer,
Frankfurt, Germany, June 16–20.
[21] JáJá, J. (1992) An Introduction to Parallel Algorithms. Addison-
Wesley, Massachusetts.
[22] Friend, E.H. (1956) Sorting on electronic computer systems.
J. ACM, 3, 134–168.
[23] Gotlieb, C. (1963) Sorting on computers. Commun. ACM, 6,
194–201.
[24] Habermann, N. (1972) Parallel Neighbor-Sort (or the Glory of
the Induction Principle). CMU Technical Report, 1, 1–12.
[25] (2008).
Paul E. Black. “Bingo Sort”. Dictionary of Algo-
rithms and Data Structures. http://xlinux.nist.gov/dads//HTML/
bingosort.html. (accessed February 26, 2020).
[26] Shell, D.L. (1959) A high-speed sorting procedure. Commun.
ACM, 2, 30–32.
[27] Williams, J.W.J. (1964) Algorithm 232: Heapsort. Commun.
ACM, 7, 347–348.
[28] Bender, M.A., Farach-Colton, M. and Mosteiro, M.A. (2006)
Insertion sort is O (n log n). Theory Comput. Syst., 39, 391–397.
[29] LaMarca, A. and Ladner, R.E. (1999) The influence of caches
on the performance of sorting. J. Algorithms, 31, 66–104.
[30] Aggarwal, A. and Vitter, J. (1988) The input/output complexity
of sorting and related problems. Commun. ACM, 31, 1116–1127.
[31] Blelloch, G.E., Fineman, J.T., Gu, Y. and Sun, Y. (2020) Opti-
mal parallel algorithms in the binary-forking model. In Proc.
of the 32nd ACM Symposium on Parallelism in Algorithms
and Architectures, pp. 89–102. ACM, Virtual Event, USA,
July 15–17.
[32] Cormen, T.H., Leiserson, C.E., Rivest, R.L. and Stein, C. (2009)
Introduction to Algorithms. MIT Press, Massachusetts.
[33] Bentley, J.L., Haken, D. and Saxe, J.B. (1980) A general method
for solving divide-and-conquer recurrences. ACM SIGACT
News, 12, 36–44.
Section A: Computer Science Theory, Methods and Tools
The Computer Journal, Vol. 65 No. 10, 2022
Downloaded from https://academic.oup.com/comjnl/article/65/10/2709/6334046 by guest on 11 May 2026


---

