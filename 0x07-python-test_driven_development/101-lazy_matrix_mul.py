#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix.

    Raises:
        ValueError: If m_a or m_b is not a list.
        ValueError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty.
        ValueError: If an element in the matrices is not an integer or a float.
        ValueError: If the matrices are not rectangular.
        ValueError: If the matrices can't be multiplied.
    """
    # Validate m_a
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise ValueError("m_a must be a list of lists")

    if any(not row or not all(isinstance(elem, (int, float)) for elem in row) for row in m_a):
        raise ValueError("m_a can't be empty and should contain only integers or floats")

    # Validate m_b
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise ValueError("m_b must be a list of lists")

    if any(not row or not all(isinstance(elem, (int, float)) for elem in row) for row in m_b):
        raise ValueError("m_b can't be empty and should contain only integers or floats")

    # Validate rectangular shape
    if any(len(row) != len(m_a[0]) for row in m_a[1:]) or any(len(row) != len(m_b[0]) for row in m_b[1:]):
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Validate multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using NumPy
    result = np.dot(m_a, m_b)

    return result.tolist()

if __name__ == "__main__":
    pass  # Add any additional code for standalone execution if needed

