Design Plan
1. Algorithm Choice: I choose Insetion sort. It is stable and it works efficiently for 25 books
2. When comparing two books, let us say, book A and book B, if A.shelfNumber < B.shelfNumber, then A comes first. if  A.shelfNumber = B.shelfNumber, then we compare the return number. if A.returnOrder < B.returnOrder, then A comes first. If two books belong to shelf5, I will compare their returnOrder. The smaller one comes first. Eg: shelf = 5, order = 2 and shelf = 5, order = 3. Then shelf = 5 , order = 2 comes first.
3. Time Complexity : Worst Case Time O(n^2) for random order (n = 25) Best Case: O(n) when already mostly sorted.
