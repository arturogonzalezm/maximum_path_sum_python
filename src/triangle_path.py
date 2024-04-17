"""
This module provides functions to calculate the maximum path sum in a triangle
and to process test cases involving such triangles.
"""

import logging


def maximum_path(triangle):
    """
    Calculate the maximum path sum from top to bottom of the triangle using a bottom-up approach.

    Args:
        triangle (list of list of int): A list of lists where each list represents a row of the triangle.

    Returns:
        int: The maximum path sum from the top to the bottom of the triangle.

    Raises:
        Exception: If an error occurs during the calculation process.
    """
    try:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
                logging.debug("After updating, row %s col %s: %s", row, col, triangle[row][col])
        return triangle[0][0]
    except Exception as e:
        logging.error("Failed to compute maximum path: %s", e)
        raise


def process_test_case(data, index):
    """
    Process a single test case from the input data, constructing the triangle and computing the maximum path sum.

    Args:
        data (list of str): The complete input data for all test cases.
        index (int): The current index in the data list to start processing this test case.

    Returns:
        tuple: Returns a tuple containing the next index after processing this test case and the result of the test case.

    Raises:
        ValueError: If there are issues with numeric conversions.
        IndexError: If there are out-of-bounds errors while accessing the data list.
        Exception: If an unexpected error occurs during processing.
    """
    try:
        num_rows = int(data[index])  # Retrieve the number of rows in the triangle
        index += 1  # Move index to the first row of the triangle
        triangle = []

        for _ in range(num_rows):
            if index >= len(data):  # Check if the index is out of range
                raise IndexError("Data index out of range while processing rows.")
            row = list(map(int, data[index].split()))
            triangle.append(row)
            index += 1  # Increment index after processing each row

        result = maximum_path(triangle)
        return index, result
    except ValueError as e:
        logging.error("Invalid input: %s", e)
        raise
    except IndexError as e:
        logging.error("Data indexing error: %s", e)
        raise
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        raise
