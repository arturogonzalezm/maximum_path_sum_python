from src.triangle_path import process_test_case
import logging
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    """
    Main function to read triangle data from a file, process it and print maximum path sums.
    """
    try:
        with open('data/input00.txt', 'r') as file:
            data = file.read().splitlines()

        index = 0
        num_cases = int(data[index])
        index += 1
        results = []

        while index < len(data):
            index, result = process_test_case(data, index)
            results.append(result)

        for result in results:
            print(result)

    except FileNotFoundError:
        logging.error("The data file was not found.")
        sys.exit(1)
    except ValueError as e:
        logging.error(f"Error processing input: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
