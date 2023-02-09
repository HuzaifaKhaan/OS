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