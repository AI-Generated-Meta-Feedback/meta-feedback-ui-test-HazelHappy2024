Test Case a – All books from different shelves
Input: [(5, 1), (2, 3), (3, 2)]
Expected Output: [(2, 3), (3, 2), (5, 1)]
Purpose: Tests sorting by shelf number as the primary key.

⸻

Test Case b – Multiple books from the same shelf (tests stability)
Input: [(2, 3), (2, 1), (2, 2)]
Expected Output: [(2, 1), (2, 2), (2, 3)]
Purpose: Tests that the algorithm preserves return order for books on the same shelf.

⸻

Test Case c – Books already in correct order
Input: [(1, 1), (2, 1), (3, 1)]
Expected Output: [(1, 1), (2, 1), (3, 1)]
Purpose: Tests best-case scenario (no swaps needed).

⸻

Test Case d – Books in reverse order
Input: [(5, 3), (4, 2), (3, 1)]
Expected Output: [(3, 1), (4, 2), (5, 3)]
Purpose: Tests worst-case scenario (maximum swaps).

