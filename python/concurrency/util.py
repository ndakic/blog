import requests
import time
from functools import wraps
from pathlib import Path

IMAGE_FOLDER = Path(".").absolute() / "files"


# CPU-bound function
def sum_square(custom_range: tuple) -> int:
    final = 0
    for i in range(custom_range[0], custom_range[1]):
        final += i * i
    return final


# I/O function
def download_image(img_url: str, save_loc: Path, image_name):
    img_url = img_url.replace("\n", "")
    img_bytes = requests.get(img_url).content
    save_loc.mkdir(parents=True, exist_ok=True)
    with open(save_loc / image_name, "wb") as img_file:
        img_file.write(img_bytes)


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        finish = time.perf_counter()
        print("==========================================================")
        print(f"\t\t\tFinished in {round(finish - start, 2)} seconds")
        print("==========================================================")

    return wrapper


def load_image_urls():
    with open(IMAGE_FOLDER / "images.txt", "r") as f:
        img_urls = f.readlines()
    return img_urls
