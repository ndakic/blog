from util import sum_square, download_image, timing, load_image_urls
from util import IMAGE_FOLDER
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

IMAGE_URLS = load_image_urls()


@timing
def sum_square_serial_run():
    result = sum_square((0, 400_000_000))
    return result


@timing
def sum_square_multiprocessing_run():
    with ProcessPoolExecutor() as pp_executor:
        mp_results = pp_executor.map(sum_square,
                                     [(0, 10000000),
                                      (10000000, 20000000),
                                      (20000000, 30000000),
                                      (30000000, 40000000)])
        mp_final_result = sum(mp_results)
        return mp_final_result


@timing
def sum_square_multithreading_run():
    with ThreadPoolExecutor() as tp_executor:
        mt_results = tp_executor.map(sum_square,
                                     [(0, 10000000),
                                      (10000000, 20000000),
                                      (20000000, 30000000),
                                      (30000000, 40000000)])
        mt_final_result = sum(mt_results)
        return mt_final_result


@timing
def download_images_serial_run():
    for i, img_url in enumerate(IMAGE_URLS):
        download_image(img_url, IMAGE_FOLDER / "serial", f"image_{i}.jpg")


@timing
def download_images_multiprocessing_run():
    with ProcessPoolExecutor() as executor:
        for i, url in enumerate(IMAGE_URLS):
            executor.submit(download_image, url, IMAGE_FOLDER / "mp", f"image_{i}.jpg")


@timing
def download_images_multithreading_run():
    with ThreadPoolExecutor() as executor:
        for i, url in enumerate(IMAGE_URLS):
            executor.submit(download_image, url, IMAGE_FOLDER / "mt", f"image_{i}.jpg")


if __name__ == "__main__":
    print("========================================================")
    print("\tsum_square (CPU-bound function) function started..")
    print("========================================================")
    result_serial = sum_square_serial_run()
    print("\tsum_square function with multiprocessing started..")
    print("========================================================")
    result_multiprocessing = sum_square_multiprocessing_run()
    print(" sum square function with multithreading started..")
    print("========================================================")
    result_multithreading = sum_square_multithreading_run()
    assert result_serial == result_multiprocessing == result_multithreading
    print("\t\tResult of all functions are equal!")
    print("==========================================================")
    print("\t download_images (I/O function) function started..")
    download_images_serial_run()
    print("\t download_images function with multiprocessing started..")
    download_images_multiprocessing_run()
    print("\t download_images function with multithreading started..")
    download_images_multithreading_run()

    """
        Results on my machine:
    ========================================================
         sum_square (CPU-bound function) function started..
    ========================================================
    ==========================================================
                Finished in 20.89 seconds
    ==========================================================
        sum_square function with multiprocessing started..
    ========================================================
    ==========================================================
                Finished in 0.61 seconds
    ==========================================================
       sum square function with multithreading started..
    ========================================================
    ==========================================================
                Finished in 2.02 seconds
    ==========================================================
            Result of all functions are equal!
    ==========================================================
         download_images (I/O function) function started..
    ==========================================================
                Finished in 33.26 seconds
    ==========================================================
      download_images function with multiprocessing started..
    ==========================================================
                Finished in 5.54 seconds
    ==========================================================
      download_images function with multithreading started..
    ==========================================================
                Finished in 3.77 seconds
    ==========================================================
        
        Conclusion: As we can see, multiprocessing is faster than multithreading in computing functions, 
                    but in IO functions, multithreading is faster than multiprocessing.
                    Use multiprocessing when you have a computing tasks, and use multithreading when you have a I/O
                    tasks.
    """