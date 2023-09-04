import random
import sys
import time

def max_pairwise_product(numbers):
    n = len(numbers)
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i

    max_index2 = -1
    for i in range(n):
        if i != max_index1 and (max_index2 == -1 or numbers[i] > numbers[max_index2]):
            max_index2 = i

    max_product = numbers[max_index1] * numbers[max_index2]

    return max_product

def generate_random_test(n):
    return [random.randint(1, 1000) for _ in range(n)]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python stress_test.py <number_of_tests>")
        sys.exit(1)

    num_tests = int(sys.argv[1])

    for test_case in range(num_tests):
        n = random.randint(2, 1000)
        test_numbers = generate_random_test(n)

        start_time = time.time()
        expected_result = max_pairwise_product(test_numbers)
        end_time = time.time()

        result = max_pairwise_product(test_numbers)

        print(f"Test {test_case + 1}:")
        print(f"Input: {test_numbers}")
        print(f"Expected: {expected_result}")
        print(f"Actual: {result}")
        print(f"Runtime: {end_time - start_time:.6f} seconds")
        print("="*40)
