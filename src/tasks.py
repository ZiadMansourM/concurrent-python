import utils
import time


@utils.time_it(logger=utils.logger)
def calculate_fibonacci(n: int) -> int:
    utils.logger.info(f"Started calculating the {n}-th Fibonacci number")
    def fib(n):
        return n if n <= 1 else fib(n-1) + fib(n-2)
    result = fib(n)
    utils.logger.info(f"Finished calculating the {n}-th Fibonacci number: {result:,}")
    return f"RESULT: The {n}-th Fibonacci number is: {result:,}"


@utils.time_it(logger=utils.logger)
def mail_letter(letter: tuple[str, int]) -> str:
    utils.logger.info(f"Started mailing letter {letter[0]} (duration: {letter[1]}s)")
    time.sleep(letter[1])
    utils.logger.info(f"Finished mailing letter {letter[0]}")
    return f"RESULT: Letter {letter[0]} mailed"
