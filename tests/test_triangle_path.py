import pytest

from src.triangle_path import maximum_path, process_test_case


def test_maximum_path_basic():
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert maximum_path(triangle) == 30, "Should calculate the correct maximum path sum"


def test_maximum_path_empty():
    with pytest.raises(Exception):
        maximum_path([]), "Should raise an exception for an empty triangle"


def test_process_test_case_basic():
    data = ["3", "3", "3 4", "6 5 7", "4 1 8 3"]
    index = 1
    new_index, result = process_test_case(data, index)
    assert result == 30, "Should return correct maximum path sum"
    assert new_index == 5, "Should update index correctly after processing"


def test_process_test_case_invalid_input():
    data = ["3", "three", "3 4", "6 5 7", "4 1 8 3"]
    index = 1
    with pytest.raises(ValueError):
        process_test_case(data, index), "Should raise ValueError for non-integer number of rows"


def test_process_test_case_out_of_bounds():
    data = ["1", "3", "3 4"]
    index = 1
    with pytest.raises(IndexError):
        process_test_case(data, index), "Should raise IndexError when accessing out of bounds"
