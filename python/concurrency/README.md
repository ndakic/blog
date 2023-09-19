# Python - Multiprocessing vs Multithreading

**TLDR: Use threading if your program is network-bound or multiprocessing if it is CPU-bound.**

## Terminologies
- Thread - A thread is a virtual version of a CPU core. Each CPU core can have up to two threads if your CPU has multi/hyper-threading enabled.
- Process - An instance of a computer program that is being executed by one or many threads.
- Multithreading - The ability of a CPU to provide multiple threads of execution concurrently, supported by the operating system.
- Multiprocessing - Ability of a system to support more than one processor or the ability to allocate tasks between them.

### Global Interpreter Lock (GIL)
- GIL is a type of process lock which is used by python whenever it deals with processes. Generally, Python only uses one thread to execute the set of written statements. 
- This means that in python only one thread will be executed at a time.
- By only allowing a single thread to be used every time we run a Python process, this ensures that only one thread can access a particular resource at a time and it also prevents the use of objects and bytecodes at once.

### Note
- Python is NOT a single-threaded language.
- Python processes typically use a single thread because of the GIL.
- Despite the GIL, libraries that perform computationally heavy tasks like numpy, scipy and pytorch utilise C-based implementations under the hood, allowing the use of multiple cores.
- Processes that are largely I/O bound benefit from multithreading while computationally heavy tasks benefit from multiprocessing.
- Python multiprocessing uses pickle to serialise/deserialize objects when passing them between processes, requiring each process to create its own copy of the data, adding substantial memory usage.
- If we want some functionality to be executed by multiple threads, and that functionality is not read-only (there are some global values which threads sharing), 
  then it is necessary to introduce a mechanism/logic that will solve the problem of changing these values at the same time. We need to introduces a lock mechanism that does not allow other threads to run until the previous thread is completed.
