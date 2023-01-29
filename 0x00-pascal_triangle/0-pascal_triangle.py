#!/usr/bin/python3
"""Defines the function pascal_triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    pascal's triangle of n
    """

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        result = []
        result.append([1])
        result.append([1, 1])

        for i in range(2, n):
            # Initialize new list
            branch = [1]
            # Define previous list
            prev = result[i - 1]

            # Iterate previous list
            for j, num in enumerate(prev):
                if j + 1 < len(prev):
                    # Add an append current element and the next element
                    branch.append(num + prev[j + 1])

            branch.append(1)
            result.append(branch)

        return result
