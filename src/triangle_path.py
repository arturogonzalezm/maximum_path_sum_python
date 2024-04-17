def maximum_path(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
            print(f"After updating, row {row} col {col}: {triangle[row][col]}")
    return triangle[0][0]


def process_test_case(data, index):
    """
    Process a single test case to read the triangle and compute the maximum path sum.

    Args:
    data (list of str): List of input strings.
    index (int): Current index in data list where the triangle starts.

    Returns:
    tuple of (int, int): Next index after processing this test case, result of the test case.
    """
    num_rows = int(data[index])
    index += 1
    triangle = []

    for _ in range(num_rows):
        row = list(map(int, data[index].split()))
        index += 1
        triangle.append(row)

    # Calculate the maximum path sum for this triangle
    result = maximum_path(triangle)
    return index, result
