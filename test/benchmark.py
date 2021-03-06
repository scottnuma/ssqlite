import argparse
import time
import random
import sfs
import string

def test_sequential_write(file_name, num_blocks, block_length):
    """Write NUM_BLOCKS block sequentially."""
    block_content = ''.join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(block_length))

    print("starting test sequential write\n")
    with sfs.open(file_name, "a") as f:
        start_time = time.time()
        for _ in range(num_blocks):
            f.write(block_content.encode('utf-8'))
        end_time = time.time()
    time_delta = end_time - start_time

    print_stats(num_blocks, block_length, time_delta)


def test_sequential_read(file_name, num_blocks, block_length):
    """Read NUM_BLOCKS blocks sequentially."""
    print("starting test sequential read\n")

    with sfs.open(file_name, "r") as f:
        start_time = time.time()
        for _ in range(num_blocks):
            f.read(block_length)
        end_time = time.time()
    time_delta = end_time - start_time

    print_stats(num_blocks, block_length, time_delta)

def test_random_read(file_name, num_blocks, block_length):
    """Read NUM_BLOCKS blocks in a random order with repeition."""
    print("starting test random read\n")
    with sfs.open(file_name, "r") as f:
        start_time = time.time()
        for _ in range(num_blocks):
            random_block_index = random.randint(0, num_blocks)
            byte_offset = random_block_index * block_length
            f.seek(byte_offset, 0)
            f.read(block_length)
        end_time = time.time()
    time_delta = end_time - start_time

    print_stats(num_blocks, block_length, time_delta)

def test_random_write(file_name, num_blocks, block_length):
    """Write NUM_BLOCKS blocks in a random order with repeition with random content."""
    print("starting test random write\n")
    block_content = ''.join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(block_length))

    with sfs.open(file_name, "w") as f:
        start_time = time.time()
        for _ in range(num_blocks):
            random_block_index = random.randint(0, num_blocks)
            byte_offset = random_block_index * block_length
            f.seek(byte_offset, 0)
            f.write(block_content.encode('utf-8'))
        end_time = time.time()
    time_delta = end_time - start_time

    print_stats(num_blocks, block_length, time_delta)

def print_stats(num_blocks, block_length, time_delta):
    print("block length: %s" % block_length)
    print("num blocks: %s" % num_blocks)

    total_bytes = num_blocks * block_length
    print("total bytes: %s" % total_bytes)

    print("elapsed time: %s" % time_delta)
    print("blocks per second: %f" % (num_blocks / time_delta))
    print("bytes per second: %f\n" % (total_bytes / time_delta))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Demonstrate of SFS read with Python')
    parser.add_argument('--mount-point', type=str, required=True,
        help='Hostname or IP address of EFS mount point')
    parser.add_argument('--test-file', type=str, required=True,
        help='File name of test file to read')
    args = parser.parse_args()

    file_name = args.test_file
    num_blocks = 32
    block_length = 32

    sfs.mount(args.mount_point)
    test_sequential_write(file_name, num_blocks, block_length)
    test_sequential_read(file_name, num_blocks, block_length)
    test_random_read(file_name, num_blocks, block_length)
    test_random_write(file_name, num_blocks, block_length)
