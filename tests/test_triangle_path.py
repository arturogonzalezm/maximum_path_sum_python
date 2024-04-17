import pytest

from src.triangle_path import maximum_path, process_test_case


def test_process_test_case_basic():
    data = ["3", "3", "3 4", "6 5 7", "4 1 8 3"]
    index = 1
    next_index, result = process_test_case(data, index)
    assert result == 22  # Adjusting the correct maximum path sum


def test_maximum_path_single_element():
    triangle = [[5]]
    assert maximum_path(triangle) == 5


def test_process_test_case_advanced():
    data = ["2", "3", "3 4", "6 5 7", "4 1 8 3"]
    index = 1
    next_index, result = process_test_case(data, index)
    assert result == 18  # Expected maximum path sum
    assert next_index == 5  # Ensuring the index after processing is correct


def test_process_test_case_incomplete_triangle():
    data = ["2", "3", "3 4", "6 5 7"]
    index = 1
    with pytest.raises(IndexError):
        process_test_case(data, index)


@pytest.mark.parametrize("triangle, expected", [
    ([[10]], 10),
    ([[10], [20, 1]], 30),
    ([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], 23)
])
def test_maximum_path_various_triangles(triangle, expected):
    assert maximum_path(triangle) == expected
