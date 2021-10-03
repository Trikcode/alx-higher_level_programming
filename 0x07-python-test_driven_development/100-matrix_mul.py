#!/usr/bin/python3
"""matrix multiplication"""


def matrix_mul(m_a, m_b):
    """matrix multiplication"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    elif m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    elif not all((isinstance(ele, int) or isinstance(ele, float))
                 for ele in [x for row in m_a for x in row]):
        raise TypeError("m_a should contain only integers or floats")
    elif not all((isinstance(ele, int) or isinstance(ele, float))
                 for ele in [x for row in m_b for x in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for row in range(len(m_b[0])):
        new_row = []
        for column in range(len(m_b)):
            new_row.append(m_b[column][row])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
