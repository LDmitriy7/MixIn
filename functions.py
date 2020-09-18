"""Various functions"""
import time
from functools import wraps, partial
from fake_headers.headers import make_header
from fake_useragent import UserAgent


def make_headers():
    """Make fake headers"""
    headers = make_header()
    headers['user-agent'] = UserAgent().chrome
    return headers


def timer(func=None, start_print=False):
    """Засекает время выполнения функции, по желанию уведомляет о начале выполнения"""
    if func is None:
        return partial(timer, start_print=start_print)

    @wraps(func)  # придает новой функции документацию, имя и сигнатуру исходной
    def wrapper(*args, **kwargs):
        if start_print:
            print(f'>> func "{func.__name__}" -> started')
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'>> func "{func.__name__}" -> finish in {time.time() - start_time:.8f}s')
        return result

    return wrapper
