import time
from functools import wraps


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} seconds")
        return result

    return wrapper


@timing
def do_calculation():
    time.sleep(2)  # Simulate some calculation
    print("Calculations finished!")


if __name__ == "__main__":
    do_calculation()
