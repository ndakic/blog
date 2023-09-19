import io
import requests
import time
import numpy as np
from functools import wraps
from PIL import Image
from pathlib import Path

IMAGE_FOLDER = Path(".").absolute() / "files"


# computing function
def sum_square(x: int) -> int:
    final = 0
    for i in range(x):
        final += i * i
    return final


# I/O function
def download_image(img_url: str, save_loc: Path) -> np.ndarray:
    img_url = img_url.replace("\n", "")
    img_bytes = requests.get(img_url).content
    save_loc.mkdir(parents=True, exist_ok=True)
    with open(save_loc / "image", "wb") as img_file:
        img_file.write(img_bytes)
    return np.array(Image.open(io.BytesIO(img_bytes)))


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        finish = time.perf_counter()
        print("=====================================================")
        print(f"Finished in {round(finish - start, 2)} seconds")
        print("=====================================================")

    return wrapper


@timing
def run_computing_function():
    sum_square(100_000_000)
    sum_square(100_000_000)
    sum_square(100_000_000)
    sum_square(100_000_000)


@timing
def run_io_function():
    with open(IMAGE_FOLDER / "images.txt", "r") as urls_file:
        urls = urls_file.readlines()
    for url in urls:
        download_image(url, IMAGE_FOLDER)
