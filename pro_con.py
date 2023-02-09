#semaphores
import threading
import random
import time

buf = []
empty = threading.Semaphore(5)
full = threading.Semaphore(0)
mutex = threading.Lock()


def producer():
    nums = range(5)
    global buf
    num = random.choice(nums)
    empty.acquire() # EMPTY ME -1
    mutex.acquire() # LOCK KARDIA SHARED RESOURCE KO
    #TAKE KOI OR ACCESS NA KAR SAKE
    buf.append(num)
    print("Produced", num, buf)
    mutex.release() # added
    full.release()  # FUL ME +1


def consumer():
    global buf
    full.acquire()
    mutex.acquire() # added
    num = buf.pop(0)
    print("Consumed", num, buf)
    mutex.release() # added
    empty.release()



consumerThread1 = threading.Thread(target=consumer)
producerThread1 = threading.Thread(target=producer)
consumerThread2 = threading.Thread(target=consumer)
producerThread2 = threading.Thread(target=producer)
producerThread3 = threading.Thread(target=producer)
producerThread4 = threading.Thread(target=producer)
producerThread5 = threading.Thread(target=producer)
producerThread6 = threading.Thread(target=producer)



consumerThread1.start()
consumerThread2.start()
producerThread1.start()
producerThread2.start()
producerThread3.start()
producerThread4.start()
producerThread5.start()
producerThread6.start()


consumerThread1.join()
consumerThread2.join()
producerThread1.join()
producerThread2.join()
producerThread3.join()
producerThread4.join()
producerThread5.join()
producerThread6.join()



# task 2

import threading
import time

readers_count = 0 # kitne reader hein db me

mutex = threading.Semaphore(1)
db = threading.Semaphore(1)

def reader(id):
    global readers_count
    mutex.acquire()
    readers_count += 1
    if readers_count == 1:
        db.acquire()
    mutex.release()

    # Reading is taking place
    print("Reader %d is reading the database." % id)
    time.sleep(1)

    mutex.acquire()
    readers_count -= 1
    if readers_count == 0:
        db.release()
    mutex.release()

def writer(id):
    db.acquire()
    # Writing is taking place
    print("Writer %d is writing to the database." % id)
    time.sleep(1)
    db.release()

reader_threads = [threading.Thread(target=reader, args=(i,)) for i in range(5)]
writer_threads = [threading.Thread(target=writer, args=(i,)) for i in range(2)]
for t in writer_threads + reader_threads :
    t.start()

for t in reader_threads + writer_threads:
    t.join()