from fei.ppds import Thread, Mutex


class Shared():
    def __init__(self, end):
        self.counter = 0
        self.end = end
        self.array = [0] * self.end
        self.mutex = Mutex()


def print_histogram(array):
    # Printing histogram of values from 0 (left) to 9 (right).

    hist = [0] * 10
    for i in array:
        hist[i] += 1

    print(hist)


def counter(shared):
    while True:

        if shared.counter >= shared.end:
            shared.mutex.unlock()
            break

        shared.mutex.lock()

        shared.array[shared.counter] += 1
        shared.counter += 1

        shared.mutex.unlock()


for _ in range(10):
    sh = Shared(1_000_000)
    t1 = Thread(counter, sh)
    t2 = Thread(counter, sh)

    t1.join()
    t2.join()

    print_histogram(sh.array)
