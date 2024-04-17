from src.triangle_path import process_test_case

if __name__ == '__main__':
    import sys

    # Change to read from a file instead of standard input
    with open('data/input00.txt', 'r') as file:
        data = file.read().splitlines()

    index = 0
    num_cases = int(data[index])
    index += 1
    results = []

    try:
        while index < len(data):
            index, result = process_test_case(data, index)
            results.append(result)
    except ValueError as e:
        print(f"Error processing input: {e}", file=sys.stderr)

    for result in results:
        print(result)
