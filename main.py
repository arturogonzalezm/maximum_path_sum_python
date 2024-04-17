"""
Module to process test cases from a file and compute the maximum path sums for triangles.
"""

import logging
import sys
from src.triangle_path import process_test_case

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    """
    Main function to read triangle data from a file, process it and print maximum path sums.
    """
    try:
        with open('data/input00.txt', 'r') as file:
            data = file.read().splitlines()

        index = 1  # Start directly from the first relevant data entry if num_cases isn't used
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
        logging.error("Error processing input: %s", e)
        sys.exit(1)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        sys.exit(1)


if __name__ == '__main__':
    main()
