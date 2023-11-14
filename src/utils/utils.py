import logging
import time
import functools

from conf import settings

logger: logging.Logger = logging.getLogger("SingletonLogger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(settings.LOGS_DIR.joinpath("tune.log"))
formatter = logging.Formatter("[%(asctime)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def time_it(logger: logging.Logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Running {func.__name__} with args: {args} and kwargs: {kwargs}")
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            logger.info(f"{func.__name__} with args: {args} and kwargs: {kwargs} ran in {end - start:,.2f}s")
            return result
        return wrapper
    return decorator