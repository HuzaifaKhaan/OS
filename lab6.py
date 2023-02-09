import os
retval = os.fork()
if retval == 0:
    print("child process is running")
    print("child prcoess ended"+ os.pid())
else:
    os.wait()
    print("child process ended")
    print("parent process now running")


#lab task 1

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


#lab task 2

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


# lab task 3

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