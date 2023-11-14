import math
import time

from conf import settings
import utils


@utils.time_it(logger=utils.logger)
def count_prime_numbers(upper_bound):
    utils.logger.info(f"Calculating prime numbers up to {upper_bound:,}")
    count = 0
    for num in range(2, upper_bound + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            count += 1
    utils.logger.info(f"Result: {count:,} prime numbers found")
    return count


@utils.time_it(logger=utils.logger)
def factorial(number):
    utils.logger.info(f"Calculating factorial of {number:,}")
    result = math.factorial(number)
    utils.logger.info(f"Result: {result:,}")
    return result


@utils.time_it(logger=utils.logger)
def calculate_fibonacci(n):
    utils.logger.info(f"Calculating the {n}-th Fibonacci number")
    
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n-1) + fib(n-2)
    
    result = fib(n)
    utils.logger.info(f"The {n}-th Fibonacci number is: {result:,}")
    return result


@utils.time_it(logger=utils.logger)
def calculate_fibonacci_efficient(n):
    utils.logger.info(f"Calculating the {n}-th Fibonacci number efficiently")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    utils.logger.info(f"The {n}-th Fibonacci number is: {a:,}")
    return a


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

if __name__ == "__main__":
    numbers = [38, 39, 40, 41, 38, 39, 40, 41]

    # Using ThreadPoolExecutor to manage threads
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(calculate_fibonacci, numbers)
    end_time = time.time()
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    # Using ProcessPoolExecutor to manage processes
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        executor.map(calculate_fibonacci, numbers)
    end_time = time.time()
    utils.logger.info(f"All processes finished and returned in  {end_time - start_time:,.2f} seconds")

