from util import sum_square, download_image, timing, load_image_urls
from util import IMAGE_FOLDER
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

IMAGE_URLS = load_image_urls()


@timing
def sum_square_serial():
    return sum_square((0, 400_000_000))


@timing
def sum_square_multiprocessing():
    with ProcessPoolExecutor() as pp_executor:
        mp_results = pp_executor.map(sum_square,
                                     [(0, 100_000_000),
                                      (100_000_000, 200_000_000),
                                      (200_000_000, 300_000_000),
                                      (300_000_000, 400_000_000)])
    return sum(mp_results)


@timing
def sum_square_multithreading():
    with ThreadPoolExecutor() as tp_executor:
        mt_results = tp_executor.map(sum_square,
                                     [(0, 100_000_000),
                                      (100_000_000, 200_000_000),
                                      (200_000_000, 300_000_000),
                                      (300_000_000, 400_000_000)])
        return sum(mt_results)


@timing
def download_images_serial():
    for i, img_url in enumerate(IMAGE_URLS):
        download_image(img_url, IMAGE_FOLDER / "serial", f"image_{i}.jpg")


@timing
def download_images_multiprocessing():
    with ProcessPoolExecutor() as executor:
        for i, url in enumerate(IMAGE_URLS):
            executor.submit(download_image, url, IMAGE_FOLDER / "mp", f"image_{i}.jpg")


@timing
def download_images_multithreading():
    with ThreadPoolExecutor() as executor:
        for i, url in enumerate(IMAGE_URLS):
            executor.submit(download_image, url, IMAGE_FOLDER / "mt", f"image_{i}.jpg")


if __name__ == "__main__":
    print("============= CPU-BOUND FUNCTION TEST ===================")
    print("\t\tsum_square function started..")
    result_serial = sum_square_serial()
    print("\tsum_square function with multiprocessing started..")
    result_multiprocessing = sum_square_multiprocessing()
    print(" sum square function with multithreading started..")
    result_multithreading = sum_square_multithreading()
    assert result_serial == result_multiprocessing == result_multithreading
    print("\t\tResult of all functions are equal!")
    print("\n\n================= I/O FUNCTION TEST ===================")
    print("\t download_images (I/O function) function started..")
    download_images_serial()
    print("\t download_images function with multiprocessing started..")
    download_images_multiprocessing()
    print("\t download_images function with multithreading started..")
    download_images_multithreading()

    """
                Results on my machine:
    
    ============= CPU-BOUND FUNCTION TEST ===================
                sum_square function started..
    ==========================================================
                Finished in 15.93 seconds
    ==========================================================
        sum_square function with multiprocessing started..
    ==========================================================
                Finished in 4.05 seconds
    ==========================================================
     sum square function with multithreading started..
    ==========================================================
                Finished in 15.32 seconds
    ==========================================================
              Result of all functions are equal!
    
    ================= I/O FUNCTION TEST ===================
         download_images (I/O function) function started..
    ==========================================================
                Finished in 9.91 seconds
    ==========================================================
         download_images function with multiprocessing started..
    ==========================================================
                Finished in 1.26 seconds
    ==========================================================
         download_images function with multithreading started..
    ==========================================================
                Finished in 0.84 seconds
    ==========================================================
        
    Conclusion: As we can see, multiprocessing is the fastest way to do CPU-bound tasks. 
                It's almost 4 times faster than serial and multithreading approaches.
                But when it comes to I/O tasks, multithreading is the fastest way to do it.
                So we can say that, if we have CPU-bound tasks, we should use multiprocessing, and if we have I/O tasks, 
                we should use multithreading.
    """
