from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import time

from conf import settings
import tasks
import utils


@utils.time_it(logger=utils.logger)
def run_cpu_bound_seq() -> None:
    results: list[int] = [
        tasks.calculate_fibonacci(number) 
        for number in settings.NUMBERS
    ]
    utils.logger.info("Fibonacci Seq Calculation Results:")
    for result in results:
        utils.logger.info(result)


@utils.time_it(logger=utils.logger)
def run_cpu_bound_map() -> None:
    start_time: float = time.time()
    with ThreadPoolExecutor() as executor:
        results: list[int] = executor.map(tasks.calculate_fibonacci, settings.NUMBERS)
    end_time: float = time.time()
    for result in results:
        utils.logger.info(result)
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    start_time: float = time.time()
    with ProcessPoolExecutor() as executor:
        results: list[int] = executor.map(tasks.calculate_fibonacci, settings.NUMBERS)
    end_time: float = time.time()
    for result in results:
        utils.logger.info(result)
    utils.logger.info(f"All processes finished and returned in  {end_time - start_time:,.2f} seconds")


@utils.time_it(logger=utils.logger)
def run_cpu_bound_as_completed() -> None:
    start_time: float = time.time()
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(tasks.calculate_fibonacci, number) 
            for number in settings.NUMBERS
        ]
        for future in as_completed(futures):
            utils.logger.info(future.result())
    end_time: float = time.time()
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    start_time: float = time.time()
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(tasks.calculate_fibonacci, number) 
            for number in settings.NUMBERS
        ]
        for future in as_completed(futures):
            utils.logger.info(future.result())
    end_time: float = time.time()
    utils.logger.info(f"All processes finished and returned in  {end_time - start_time:,.2f} seconds")


@utils.time_it(logger=utils.logger)
def run_io_bound_seq() -> None:
    results: list[str] = [
        tasks.mail_letter(letter) 
        for letter in settings.LETTERS
    ]

    utils.logger.info("Mailing Results:")
    for result in results:
        utils.logger.info(result)


@utils.time_it(logger=utils.logger)
def run_io_bound_map() -> None:
    start_time: float = time.time()
    with ThreadPoolExecutor() as executor:
        results: list[str] = executor.map(tasks.mail_letter, settings.LETTERS)
    end_time: float = time.time()
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    utils.logger.info("Mailing Results:")
    for result in results:
        utils.logger.info(result)

    start_time: float = time.time()
    with ProcessPoolExecutor() as executor:
        results: list[str] = executor.map(tasks.mail_letter, settings.LETTERS)
    end_time: float = time.time()
    utils.logger.info(f"All processes finished and returned in  {end_time - start_time:,.2f} seconds")

    utils.logger.info("Mailing Results:")
    for result in results:
        utils.logger.info(result)


@utils.time_it(logger=utils.logger)
def run_io_bound_as_completed() -> None:
    start_time: float = time.time()
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(tasks.mail_letter, letter) 
            for letter in settings.LETTERS
        ]
        for future in as_completed(futures):
            utils.logger.info(future.result())
    end_time: float = time.time()
    utils.logger.info(f"All threads finished and returned in {end_time - start_time:,.2f} seconds")

    start_time: float = time.time()
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(tasks.mail_letter, letter) 
            for letter in settings.LETTERS
        ]
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
