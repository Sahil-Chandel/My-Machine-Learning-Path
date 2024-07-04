'''
REAL-WORLD EXAMPLE :    Multiprocessor for CPU-bound Tasks
SCENARIO:   factorial calculation
            factorial calculation, especially for large numbers,
            involve significiant computional work. Multiprocessing
            can be used to distribute the workload across multiple
            CPU cores, improving performance
'''

import _multiprocessing
import math
import sys
import time

#Increase the maximum number of integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorial of a given number

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]

    start_time = time.time()

    ##create a pool of worker processes
    with _multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
