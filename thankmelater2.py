# =========================  simple child process ===============================================

import os

retval = os.fork()
if retval == 0:
    print("child process is running")
    print("child prcoess ended" + os.pid())
else:
    os.wait()
    print("child process ended")
    print("parent process now running")

# ================================= zombie process 10 second wait ===============================================

# Using either a Linux system, write a program that forks a child process that ultimately becomes a zombie process.
# This zombie process must remain in the system for at least 10 seconds.

import os
import time

pid = os.fork()

if pid == 0:
    # This is the child process
    print("Child process, pid =", os.getpid())
    # Exit immediately, becoming a zombie process
    os._exit(0)
else:
    # This is the parent process
    print("Parent process, pid =", os.getpid())
    # Wait for 10 seconds
    time.sleep(10)
    # Check the status of the child process
    pid, status = os.waitpid(pid, os.WSTOPSIG | os.WEXITED)
    print("Child process has finished with status:", status)

# ================================== child k 2 child ===============================================

#  Write a program that creates a child process which further creates its two child processes. Store the process id of
# each process in an array called Created Processes. Also display the process id of the terminated child to
# understand the hierarchy of termination of each child process.

import os
import time

created_processes = []

pid = os.fork()

if pid == 0:
    # This is the first child process
    print("First child process, pid =", os.getpid())
    created_processes.append(os.getpid())

    # Create the second child process
    pid1 = os.fork()
    if pid1 == 0:
        # This is the second child process
        print("Second child process, pid =", os.getpid())
        created_processes.append(os.getpid())

        # Create the third child process
        pid2 = os.fork()
        if pid2 == 0:
            # This is the third child process
            print("Third child process, pid =", os.getpid())
            created_processes.append(os.getpid())

            # Exit immediately
            os._exit(0)
        else:
            # Wait for the third child process to exit
            pid3, status = os.waitpid(pid2, os.WSTOPSIG | os.WEXITED)
            print("Third child process has finished with pid:", pid3)
            # Exit immediately
            os._exit(0)
    else:
        # Wait for the second child process to exit
        pid2, status = os.waitpid(pid1, os.WSTOPSIG | os.WEXITED)
        print("Second child process has finished with pid:", pid2)
        # Exit immediately
        os._exit(0)
else:
    # Wait for the first child process to exit
    pid1, status = os.waitpid(pid, os.WSTOPSIG | os.WEXITED)
    print("First child process has finished with pid:", pid1)
    # Print the list of created processes
    print("Created processes:", created_processes)

# ============ array create in parent , sort in child =============================================

# . Write a program in which a parent process will initialize an array, and child process will sort this array. Use wait()
# and sleep() methods to achieve the synchronization such that parent process should run first.

import os
import time

# Initialize the array in the parent process
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Array before sorting:", arr)

pid = os.fork()

if pid == 0:
    # This is the child process
    print("Child process, pid =", os.getpid())

    # Sort the array
    arr.sort()

    # Wait for 1 second
    time.sleep(1)
    print("Array after sorting:", arr)
    # Exit immediately
    os._exit(0)
else:
    # This is the parent process
    print("Parent process, pid =", os.getpid())

    # Wait for the child process to exit
    os.wait()

    # Wait for 1 second
    time.sleep(1)
    print("Array after sorting:", arr)

################## THREADING ###################################################################################
##############################################################################################################

# ============  2 thread aik sey name aik sey roll no===============================

# Modify Example 1 to display strings via two independent threads:
# thread1: “Hello ! StudentName___”, thread 2: “Student roll no is :__________”

import threading


def name_fun(name):
    print(f"hello studentName{name}")


def roll_fun(roll):
    print(f"student roll no is", roll)


t1 = threading.Thread(target=name_fun, args=("name",))
t2 = threading.Thread(target=roll_fun, args=(1,));
t1.start()
t2.start()
t2.join()
t2.join()


# ============  no of threads by user ==============

# Create threads message as many times as user wants to create threads by using array of threads and loop.
# Threads should display message that is passed through argument.

def create_tr(n):
    print(f"hello \n thread number : {n}")


n = int(input("enter no of thread :  "))
thread_li = []
for i in range(n):
    t1 = threading.Thread(target=create_tr, args=(i,))
    t1.start()
    thread_li.append(t1)

for i in thread_li:
    i.join()

################## SEMAPHORE ##################################################################################
##############################################################################################################

# ============ PRODUCER CONSUMER =================================

# Write a python program that demonstrates the synchronization of Consumer producer Bounded Buffer
# Problem using semaphores

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
    empty.acquire()  # EMPTY ME -1
    mutex.acquire()  # LOCK KARDIA SHARED RESOURCE KO
    # TAKE KOI OR ACCESS NA KAR SAKE
    buf.append(num)
    print("Produced", num, buf)
    mutex.release()  # added
    full.release()  # FUL ME +1


def consumer():
    global buf
    full.acquire()
    mutex.acquire()  # added
    num = buf.pop(0)
    print("Consumed", num, buf)
    mutex.release()  # added
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

# ============ READ WRITE BINARY SEMAPHORE============================

# Write a python program that demonstrates the synchronization of Readers and Writer Problem using
# semaphores.

import threading
import time

readers_count = 0  # kitne reader hein db me

db = threading.Semaphore(1)
mutex = threading.Lock()


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
for t in writer_threads + reader_threads:
    t.start()

for t in reader_threads + writer_threads:
    t.join()

###################### INTERPROCESS COMMUNCITON PIPE  ##################################################################
##############################################################################################################

import os

r, w = os.pipe()
ret = os.fork()

if ret > 0:
    os.close(r)

    print("parent")
    text = "hello child ".encode()

    os.write(w, text)
    os.close(w)

else:
    os.close(w)
    print("child")
    cr = os.fdopen(r)

    print(cr.read())

# ================ LAB 11 PARENT CHILD KI COMMUNICATION THROUGH MULTIPROCESSING =====================

try:
    from multiprocessing import Process, Pipe
except:
    os.system("pip install multiprocessing")


def f(child_conn):
    print(child_conn.recv())
    child_conn.send("hello parent")
    child_conn.close()


p_conn, c_conn = Pipe()
p_conn.send("hello child")

p1 = Process(target=f, args=(c_conn,))

p1.start()
p1.join()

print(p_conn.recv())
p_conn.close()

# ======================== LAB 11 PARENT LIST BANA RAH CHILD SORT KARRAH ============================

from multiprocessing import Process, Array, Value, Pipe


def child_process(arr, n, c):
    arr = sorted(arr[:], reverse=True)
    print(arr[:])
    for i in range(len(arr)):
        arr[i] = -arr[i]
    n = n.value + 1.1

    print("abba ne ye bola ", c.recv())
    c.send((arr, n))
    c.close()


p_conn, c_conn = Pipe()
p_conn.send("chal shaba reverse sort kar ke de or value me +1")

arr = Array('i', range(10))
print(arr[:])
n = Value('d', 2.0)
p1 = Process(target=child_process, args=(arr, n, c_conn,))

p1.start()
p1.join()
print(p_conn.recv())
p_conn.close()

# ======================== Lab 11 os.pipe se do pipe bana raahe=========================


import os

r, w = os.pipe()
r2, w2 = os.pipe()
pid = os.fork()

if pid > 0:
    os.close(w2)  # un-necessary chezon ko pehle band kro
    os.close(r)
    print('Parent process is writing')
    text = 'Hello child proces'.encode()
    os.write(w, text)
    os.close(w)
    pr = os.fdopen(r2)
    print('Child has sent ', pr.read())

else:
    os.close(w)  # un-necessary chezon ko pehle band kro
    os.close(r2)
    print('\nChild process ')
    cr = os.fdopen(r)
    print('Read', cr.read())
    print('\nChild process is sending regards')
    text = 'Thankyou'.encode()
    os.write(w2, text)
    os.close(w2)

##LAB 11 5 FUNCTIONS ME SHARED VALUE JA RAHI OR +1 HO RAH

from multiprocessing import Process, Value


def t1(value):
    value.value += 1


def t2(value):
    value.value += 1


def t3(value):
    value.value += 1


def t4(value):
    value.value += 1


def t5(value):
    value.value += 1


v = Value('i', 0)
print(v.value)
p1 = Process(target=t1, args=(v,))
p2 = Process(target=t2, args=(v,))
p3 = Process(target=t3, args=(v,))
p4 = Process(target=t4, args=(v,))
p5 = Process(target=t5, args=(v,))

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()

print(v.value)

LAB
12
2
PROCESSES
BAN
RAHE
DONO
ME
ADHI
ADHI
LIST
JA
RAHI
OR
SQUARE
HO
RAH

from multiprocessing import Process, Array
import random


def square(arr, i, j):
    print(arr[i:j])
    for i in range(i, j):
        arr[i] = arr[i] ** 2


arr = Array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[:])
p1 = Process(target=square, args=(arr, 0, len(arr[:]) // 2,))
p2 = Process(target=square, args=(arr, (len(arr[:]) // 2), len(arr[:]),))

p1.start()
p2.start()
p1.join()
p2.join()
print(arr[:])

COMMAND
LINE
SE
INPUT
LE
RAHE

import sys
from multiprocessing import Process, Pipe


def parent(conn, name):
    print("parent")
    conn.send(name)
    conn.close()


def child(conn):
    print("child")
    print(conn.recv())
    conn.close()


name = sys.argv[1]
p_conn, c_conn = Pipe()
p = Process(target=parent, args=(p_conn, name,))
c = Process(target=child, args=(c_conn,))

p.start()
c.start()

p.join()
c.join()

###################### MULTIPROCESS INTERPROCESS SHARED MEMORY ##################################################################
##############################################################################################################


# LAB 12 =================================== 2 PROCESSES BAN RAHE DONO ME ADHI ADHI LIST JA  RAHI OR SQUARE HO RAH =======================

from multiprocessing import Process, Array
import random


def square(arr, i, j):
    print(arr[i:j])
    for i in range(i, j):
        arr[i] = arr[i] ** 2


arr = Array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[:])
p1 = Process(target=square, args=(arr, 0, len(arr[:]) // 2,))
p2 = Process(target=square, args=(arr, (len(arr[:]) // 2), len(arr[:]),))

p1.start()
p2.start()
p1.join()
p2.join()
print(arr[:])

# ============================ COMMAND LINE SE INPUT LE RAHE ======================================================


import sys
from multiprocessing import Process, Pipe


def parent(conn, name):
    print("parent")
    conn.send(name)
    conn.close()


def child(conn):
    print("child")
    print(conn.recv())
    conn.close()


name = sys.argv[1]
p_conn, c_conn = Pipe()
p = Process(target=parent, args=(p_conn, name,))
c = Process(target=child, args=(c_conn,))

p.start()
c.start()

p.join()
c.join()


###################### BANKER ALGORITHM  ##################################################################
##############################################################################################################

def is_safe_state(processes, avail, need, allot):
    """
    Check if the system is in a safe state
    :param processes: Number of processes
    :param avail: Available resources
    :param need: Need matrix for each process
    :param allot: Allocation matrix for each process
    :return: True if safe state, False otherwise
    """
    # Mark all processes as infeasible
    finish = [False] * processes

    # To store safe sequence
    safe_seq = [0] * processes

    # Make a copy of available resources
    work = [0] * len(avail)
    for i in range(len(avail)):
        work[i] = avail[i]

    # While all processes are not finished or system is not in safe state
    count = 0
    while count < processes:
        # Find a process which is not finish and whose needs can be satisfied with current work[]
        found = False
        for p in range(processes):
            if finish[p] == False and need[p][:len(work)] <= work:
                # Add the allocated resources of current P to the available/work resources i.e. free the resources
                for j in range(len(work)):
                    work[j] += allot[p][j]

                # Add this process to safe sequence.
                safe_seq[count] = p
                count += 1

                # Mark this p as finished
                finish[p] = True
                found = True

        # If we could not find a next process in safe sequence.
        if found == False:
            print("System is not in safe state")
            return False

    # If system is in safe state then safe sequence will be as below
    print("System is in safe state.\nSafe sequence is: ", end=" ")
    print(*safe_seq)

    return True


# Driver code
if __name__ == '__main__':
    processes = 5
    avail = [3, 3, 2]
    max_res = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    allot = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

    # Calculate the need matrix
    need = []
    for i in range(processes):
        n = [max_res[i][j] - allot[i][j] for j in range(len(avail))]
        need.append(n)

    # Check system is in safe state or not
    is_safe_state(processes, avail, need, allot)