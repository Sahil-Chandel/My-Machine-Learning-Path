## processes that  run in parallel
## CPU-Bound Tasks that are heavy on CPU usage(eg:- mathematical computation, data processing )
## Parallel execution- Multiple cores of the cpu

import multiprocessing
import multiprocessing.process
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")

def cube_letter():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube:{i * i * i}")

if __name__=="__main__":
        
        ## create 2 processes
        p1 = multiprocessing.Process(target=square_numbers)
        p2 = multiprocessing.Process(target=cube_letter)


        t = time.time()
        ## start the thread
        p1.start()
        p2.start()

        ## wait for the threads to complete
        p1.join()
        p2.join()


        finished_time=time.time()-t
        print(finished_time)
