from util import sum_square, download_image, timing, run_computing_function, run_io_function
from util import IMAGE_FOLDER
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


@timing
def use_multiprocessing_on_computing_function():
    with ProcessPoolExecutor() as executor:
        results = executor.map(sum_square, [100_000_000, 100_000_000, 100_000_000, 100_000_000])


@timing
def use_multiprocessing_on_io_function():
    with open(IMAGE_FOLDER / "images.txt", "r") as f:
        img_urls = f.readlines()
    with ProcessPoolExecutor() as executor:
        for url in img_urls:
            executor.submit(download_image, url, IMAGE_FOLDER)


@timing
def use_multithreading_on_computing_function():
    with ThreadPoolExecutor() as executor:
        results = executor.map(sum_square, [100_000_000, 100_000_000, 100_000_000, 100_000_000])


@timing
def use_multithreading_on_io_function():
    with open(IMAGE_FOLDER / "images.txt", "r") as f:
        img_urls = f.readlines()

    with ThreadPoolExecutor() as executor:
        for url in img_urls:
            executor.submit(download_image, url, IMAGE_FOLDER)


if __name__ == "__main__":
    print("========================================================")
    print("\t\tComputing function started..")
    run_computing_function()
    print("Use multiprocessing on computing function started..")
    use_multiprocessing_on_computing_function()
    print("Use multithreading on computing function started..")
    use_multithreading_on_computing_function()
    print("\t\tTesting io function started")
    run_io_function()
    print("Testing multiprocessing on io function started")
    use_multiprocessing_on_io_function()
    print("Testing multithreading on io function started")
    use_multithreading_on_io_function()

    """
        Results on my machine:
        ========================================================
                Computing function started..
        =====================================================
        Finished in 15.79 seconds
        =====================================================
        Use multiprocessing on computing function started..
        =====================================================
        Finished in 4.42 seconds
        =====================================================
        Use multithreading on computing function started..
        =====================================================
        Finished in 15.47 seconds
        =====================================================
                Testing io function started
        =====================================================
        Finished in 19.07 seconds
        =====================================================
        Testing multiprocessing on io function started
        =====================================================
        Finished in 2.78 seconds
        =====================================================
        Testing multithreading on io function started
        =====================================================
        Finished in 1.47 seconds
        =====================================================
        
        Conclusion: As we can see, multiprocessing is faster than multithreading in computing functions, 
                    but in IO functions, multithreading is faster than multiprocessing.
                    Use multiprocessing when you have a lot of computing tasks, and use multithreading when you have a 
                    lot of IO tasks.
    """