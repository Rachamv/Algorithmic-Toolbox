import random
import sys
import os
import time

def generate_test(seed, n):
    random.seed(seed)
    print(n)
    print(' '.join(str(random.randint(2, 100)) for _ in range(n)))

def run_main_solution(input_file):
    start_time = time.time()  # Start measuring execution time
    os.system(f"python3 main.py < {input_file} > main_output.txt")
    end_time = time.time()  # Stop measuring execution time

    with open('main_output.txt', 'r') as f:
        main_output = f.read()

    return main_output, end_time - start_time

def is_output_correct(main_output, expected_output):
    return main_output.strip() == expected_output.strip()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python test_script.py 10 <seed> <expected_output>")
        sys.exit(1)

    test_size = int(sys.argv[1])
    seed = int(sys.argv[2])
    expected_output = sys.argv[3]

    generate_test(seed, test_size)
    os.system(f"python generate_test.py {test_size} {seed} > input.txt")

    main_output, execution_time = run_main_solution("input.txt")

    if is_output_correct(main_output, expected_output):
        print(f"Test passed! Execution time: {execution_time:.6f} seconds")
    else:
        print(f"Test failed! Execution time: {execution_time:.6f} seconds")
