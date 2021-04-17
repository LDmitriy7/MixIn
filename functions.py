"""Various functions"""
import time
from functools import wraps, partial


def timer(func=None, start_print=False, printer=print):
    """Засекает время выполнения функции, по желанию уведомляет о начале выполнения"""
    if func is None:
        return partial(timer, start_print=start_print)

    @wraps(func)  # придает новой функции документацию, имя и сигнатуру исходной
    def wrapper(*args, **kwargs):
        if start_print:
            printer(f'>> func "{func.__name__}" -> started')
        start_time = time.time()
        result = func(*args, **kwargs)
        printer(f'>> func "{func.__name__}" -> finish in {time.time() - start_time:.8f}s')
        return result

    return wrapper
