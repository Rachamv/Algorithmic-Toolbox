import random
import sys
import time

def sum_of_two_digits(a, b):
    return a + b

def generate_random_test():
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    return a, b

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python generate_test_sum.py <number_of_tests>")
        sys.exit(1)

    num_tests = int(sys.argv[1])

    for test_case in range(num_tests):
        a, b = generate_random_test()

        print(f"Test {test_case + 1}:")
        print(f"Input: a={a}, b={b}")
        expected_result = sum_of_two_digits(a, b)
        print(f"Expected: {expected_result}")
        start_time = time.time()
        result = sum_of_two_digits(a, b)
        end_time = time.time()
        print(f"Actual: {result}")
        print(f"Runtime: {end_time - start_time:.6f} seconds")
        print("="*40)
