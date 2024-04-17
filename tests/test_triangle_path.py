"""
Uni tests for the triangle_path module.
"""

import pytest
from src.triangle_path import maximum_path, process_test_case


def test_maximum_path_simple():
    """
       Test the maximum_path function with a standard triangle.
       Ensures it calculates the correct maximum path sum.
       """
    triangle = [[2], [4, 1], [3, 9, 7]]
    assert maximum_path(triangle) == 15


def test_maximum_path_empty():
    """
    Test the maximum_path function with an empty triangle.
    Expects an IndexError to be raised due to the empty input.
    """
    with pytest.raises(IndexError):
        maximum_path([])


def test_process_test_case_basic():
    """
    Test the process_test_case function with valid input data.
    Checks if it correctly processes the input and returns the correct sum and index.
    """
    data = ["3", "3", "1 2", "4 5 6", "7 8 9"]
    index = 1
    new_index, result = process_test_case(data, index)
    assert new_index == 5  # Confirm the index is correct after processing
    assert result == 15  # Assuming the maximum path calculation is correct for your triangle implementation


def test_process_test_case_invalid_input():
    """
    Test the process_test_case function with invalid input.
    Checks for ValueError when non-numeric values are provided where integers are expected.
    """
    data = ["2", "three", "1 2 3", "4 5 6 7"]
    index = 1
    with pytest.raises(ValueError):
        process_test_case(data, index)


def test_process_test_case_out_of_bounds():
    """
    Test the process_test_case function for handling out-of-bounds errors.
    Ensures it raises IndexError when the function attempts to access data beyond the list's range.
    """
    data = ["1", "2", "10"]
    index = 1
    with pytest.raises(IndexError):
        process_test_case(data, index)
