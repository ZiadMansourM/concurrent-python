from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import time

import utils


@utils.time_it(logger=utils.logger)
def calculate_fibonacci(n: int) -> int:
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
def run_cpu_bound_seq() -> None:
    numbers: list[int] = [38, 39, 40, 41]

    results: list[int] = [calculate_fibonacci(number) for number in numbers]

    utils.logger.info("Fibonacci Calculation Results:")
    for result in results:
        utils.logger.info(result)


@utils.time_it(logger=utils.logger)
def run_cpu_bound_map() -> None:
    numbers: list[int] = [38, 39, 40, 41]

    start_time: float = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(calculate_fibonacci, numbers)
    end_time: float = time.time()
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    start_time: float = time.time()
    with ProcessPoolExecutor() as executor:
        executor.map(calculate_fibonacci, numbers)
    end_time: float = time.time()
    utils.logger.info(f"All processes finished and returned in  {end_time - start_time:,.2f} seconds")


@utils.time_it(logger=utils.logger)
def run_cpu_bound_as_completed() -> None:
    numbers: list[int] = [38, 39, 40, 41]

    start_time: float = time.time()
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(calculate_fibonacci, number) for number in numbers]
        for future in as_completed(futures):
            utils.logger.info(future.result())
    end_time: float = time.time()
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    start_time: float = time.time()
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(calculate_fibonacci, number) for number in numbers]
        for future in as_completed(futures):
            utils.logger.info(future.result())
    end_time: float = time.time()
    utils.logger.info(f"All processes finished and returned in  {end_time - start_time:,.2f} seconds")


@utils.time_it(logger=utils.logger)
def mail_letter(letter: tuple[str, int]) -> str:
    utils.logger.info(f"Started mailing letter {letter[0]} (duration: {letter[1]}s)")
    time.sleep(letter[1])
    utils.logger.info(f"Finished mailing letter {letter[0]}")
    return f"Letter {letter[0]} mailed"


@utils.time_it(logger=utils.logger)
def run_io_bound_seq() -> None:
    letters: dict[str, int] = {'A': 4, 'B': 5, 'C': 3, 'D': 2, 'E': 3}
    
    results: list[str] = [mail_letter(letter) for letter in letters.items()]

    utils.logger.info("Mailing Results:")
    for result in results:
        utils.logger.info(result)


@utils.time_it(logger=utils.logger)
def run_io_bound_map() -> None:
    letters: dict[str, int] = {'A': 4, 'B': 5, 'C': 3, 'D': 2, 'E': 3}

    start_time: float = time.time()
    with ThreadPoolExecutor() as executor:
        results: list[str] = executor.map(mail_letter, letters.items())
    end_time: float = time.time()
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    utils.logger.info("Mailing Results:")
    for result in results:
        utils.logger.info(result)

    start_time: float = time.time()
    with ProcessPoolExecutor() as executor:
        results: list[str] = executor.map(mail_letter, letters.items())
    end_time: float = time.time()
    utils.logger.info(f"All processes finished and returned in  {end_time - start_time:,.2f} seconds")

    utils.logger.info("Mailing Results:")
    for result in results:
        utils.logger.info(result)


@utils.time_it(logger=utils.logger)
def run_io_bound_as_completed() -> None:
    letters: dict[str, int] = {'A': 4, 'B': 5, 'C': 3, 'D': 2, 'E': 3}

    start_time: float = time.time()
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(mail_letter, letter) for letter in letters.items()]
        for future in as_completed(futures):
            utils.logger.info(future.result())
    end_time: float = time.time()
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    start_time: float = time.time()
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(mail_letter, letter) for letter in letters.items()]
        for future in as_completed(futures):
            utils.logger.info(future.result())
    end_time: float = time.time()
    utils.logger.info(f"All processes finished and returned in  {end_time - start_time:,.2f} seconds")


@utils.time_it(logger=utils.logger)
def main() -> None:
    utils.logger.info("------> Running I/O Bound Tasks")
    run_io_bound_seq()
    run_io_bound_map()
    run_io_bound_as_completed()

    utils.logger.info("------> Running CPU Bound Tasks")
    run_cpu_bound_seq()
    run_cpu_bound_map()
    run_cpu_bound_as_completed()


if __name__ == "__main__":
    main()
