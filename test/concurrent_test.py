"""
Test concurrently mounting, reading, and writing.

We assume the logs folder exists, and that /test/ exists on EFS.
"""

import os
import time
import multiprocessing
import logging

def simple_read_write():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(levelname)s\t%(filename)s:%(lineno)d:%(funcName)s\t%(message)s",
                        datefmt='%m-%d %H:%M',
                        filename="logs/{}.log".format(os.getpid()),
                        filemode='w')


    logging.info("starting simple_read_write on thread %s", os.getpid())
    import sfs
    sfs.mount(os.environ["NFS4_SERVER"])
    file_name = "/test/simple_read_write_{}.txt".format(os.getpid())

    f = sfs.open(file_name, "w")
    content = "hello world at {}".format(time.time())
    f.write(content)
    f.close()

    f = sfs.open(file_name, "r")
    read_content = f.read()
    if content == read_content:
        logging.info("read write successful")
    else:
        logging.error("read write failed")

def multi_write():
    workers = []
    num_workers = 16
    for _ in range(num_workers):
        workers.append(multiprocessing.Process(target=simple_read_write))
    for _, worker in enumerate(workers):
        worker.start()
    for _, worker in enumerate(workers):
        worker.join()

def clear_log_folder():
    mydir = "logs"
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".log") ]
    for f in filelist:
        print("removing", f)
        os.remove(os.path.join(mydir, f))

if __name__ == "__main__":
    clear_log_folder()
    multi_write()
