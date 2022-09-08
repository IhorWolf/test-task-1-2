"""
What is FOR loop?
You have a positive integer number N as an input. Please write a program in Python 3 that calculates the sum in range 1 and N.

Examples: Input: 1 Output: 1
Input: 3 Output: 6
Input 10: Output: 55
"""
n = int(input())
m = 0
for i in range(n+1): 
    m+=i
print(m)

"""
Counting islands

Inputs: M N Matrix
You have a matrix MxN that represents a map. There are 2 possible states on the map: 1 - islands, 0 - ocean. Your task is to calculate the number of islands in the most effective way. Please write code in Python 3.
Examples: Input:

3 3
0 1 0
0 0 0
0 1 1

Output: 2

Input:

3 4
0 0 0 1
0 0 1 0
0 1 0 0

Output: 3

Input:
3 4
0 0 0 1
0 0 1 1
0 1 0 1
Output: 2


"""
from collections import deque
rows, cols = map(int, input().split())
matrix = [[i for i in input().split()] for _ in range(rows)]
v = set()
islands = 0
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == '1' and (r, c) not in v:
            islands += 1
            q = deque()
            v.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                direct = [[1, 0],[-1, 0], [0, 1], [0, -1]]
                for row_d, col_d in direct:
                    r, c = row + row_d, col + col_d
                    if (r in range(rows) and c in range(cols) 
                        and matrix[r][c] == '1' and (r, c) not in v):
                        q.append((r, c))
                        v.add((r, c))
print(islands)