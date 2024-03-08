#!/usr/bin/python3
'''A module for working with pascals triangle'''

def pascal_triangle(n: int) -> List[list]:
    '''Pascal triangle, creates a list of integers representing the Pascal's triangle of a given integer.
    '''
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(0, len(triangle[-1])-1):
            a = triangle[-1][j]
            b = triangle[-1][j+1]
            temp.insert(-1, a + b)
        triangle.append(temp)

    return triangle
