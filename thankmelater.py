import os

try:
    from rich.console import Console
    from rich.table import Table
    import pyfiglet as pyg
    from operator import attrgetter
except ImportError:
    os.system("pip install rich")
    os.system("pip install pyfiglet")
    os.system("pip install operator")
    from rich.console import Console
    from rich.table import Table
    import pyfiglet as pyg

os.system("cls")


# res= pyg.figlet_format("SJF Algorithm", font = "slant")
# print(res)

class Process:
    def __init__(self, pid=0, arrival_time=0, burst_time=0, priority=0):
        self.pid: int = pid
        self.arrival_time: int = arrival_time
        self.burst_time: int = burst_time
        self.waiting_time: int = 0
        self.turnaround_time: int = 0
        self.completion_time: int = 0
        self.priority: int = priority


class Algorithems:

    def __init__(self):

        self.console = Console()

        self.table = Table(show_header=True, header_style="bold magenta")
        self.table.add_column("Process")
        self.table.add_column("Arrival Time")
        self.table.add_column("Burst Time")
        self.table.add_column("Completion Time")
        self.table.add_column("Turn Around Time")
        self.table.add_column("Waiting Time")
        self.table.add_column("Priority")

    def priority(self):
        processes = []
        n = int(input("Enter the number of processes: "))
        for i in range(0, n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))
            priority = int(input("Enter the Priority: "))
            processes.append(Process(i + 1, arrival_time=at, burst_time=burst_time, priority=priority))

        processes.sort(key=attrgetter("priority"))

        for i in range(len(processes)):
            try:
                # processes[i].completion_time = processes[i-1].completion_time + processes[i].burst_time
                if processes[i].arrival_time <= processes[i - 1].completion_time:
                    processes[i].completion_time = processes[i - 1].completion_time + processes[i].burst_time
                else:

                    processes[i].completion_time = processes[i].arrival_time + processes[i].burst_time
                processes[i].turnaround_time = processes[i].completion_time - processes[i].arrival_time
                processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time
            except:
                pass
        self.draw(processes)

    def SJF_beta(self):
        processes = []
        n = int(input("Enter the number of processes: "))
        for i in range(0, n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))
            processes.append(Process(i + 1, arrival_time=at, burst_time=burst_time))

        processes.sort(key=attrgetter("arrival_time"))
        processes2 = processes.copy()
        timer = processes[0].arrival_time
        completed = []
        while True:
            if len(processes2) == 0:
                break
            arrived = []
            for i in processes2:
                if i.arrival_time <= timer:
                    arrived.append(i)

            minimum_burst = min(arrived, key=attrgetter("burst_time"))
            minimum_burst.completion_time = minimum_burst.burst_time + timer
            timer = minimum_burst.completion_time
            minimum_burst.turnaround_time = minimum_burst.completion_time - minimum_burst.arrival_time
            minimum_burst.waiting_time = minimum_burst.turnaround_time - minimum_burst.burst_time
            completed.append(minimum_burst)
            processes2.remove(minimum_burst)

        self.draw(completed)

    def priority_pre_beta(self):
        processes = []
        processes2 = []
        n = int(input("Enter the number of processes: "))
        for i in range(0, n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))
            priority = int(input("Enter the Priority: "))
            processes.append(Process(i + 1, arrival_time=at, burst_time=burst_time, priority=priority))
            processes2.append(Process(i + 1, arrival_time=at, burst_time=burst_time, priority=priority))

        processes.sort(key=attrgetter("arrival_time"))
        processes2.sort(key=attrgetter("arrival_time"))

        timer = processes[0].arrival_time
        completed = []
        while True:
            if len(processes2) == 0:
                break
            arrived = []
            for i in processes2:
                if i.arrival_time <= timer:
                    arrived.append(i)
            minimum_prority = min(arrived, key=attrgetter("priority"))
            minimum_prority.burst_time = minimum_prority.burst_time - 1
            minimum_prority.completion_time = timer + 1
            if minimum_prority.burst_time <= 0:
                arrived.remove(minimum_prority)
                completed.append(minimum_prority)
                processes2.remove(minimum_prority)
            timer += 1
        completed.sort(key=attrgetter("arrival_time"))
        for z, item in enumerate(completed):
            item.burst_time = processes[z].burst_time
            item.turnaround_time = item.completion_time - item.arrival_time
            item.waiting_time = abs(item.turnaround_time - item.burst_time)
        self.draw(completed)

    def SJF_pre_beta(self):
        processes = []
        processes2 = []
        n = int(input("Enter the number of processes: "))
        for i in range(0, n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))
            processes.append(Process(i + 1, arrival_time=at, burst_time=burst_time))
            processes2.append(Process(i + 1, arrival_time=at, burst_time=burst_time))

        processes.sort(key=attrgetter("arrival_time"))

        processes2.sort(key=attrgetter("arrival_time"))

        timer = processes[0].arrival_time
        completed = []
        while True:
            if len(processes2) == 0:
                break
            arrived = []
            for i in processes2:
                if i.arrival_time <= timer:
                    arrived.append(i)
            minimum_burst = min(arrived, key=attrgetter("burst_time"))
            minimum_burst.burst_time = minimum_burst.burst_time - 1
            minimum_burst.completion_time = timer + 1
            if minimum_burst.burst_time <= 0:
                arrived.remove(minimum_burst)
                completed.append(minimum_burst)
                processes2.remove(minimum_burst)
            timer += 1
        completed.sort(key=attrgetter("arrival_time"))
        for z, item in enumerate(completed):
            item.burst_time = processes[z].burst_time
            item.turnaround_time = item.completion_time - item.arrival_time
            item.waiting_time = abs(item.turnaround_time - item.burst_time)
        self.draw(completed)

    def draw(self, processes):

        for process in processes:
            self.table.add_row(
                f"P{process.pid}",
                f"{process.arrival_time}",
                f"{process.burst_time}",
                f"{process.completion_time}",
                f"{process.turnaround_time}",
                f"{process.waiting_time}",
                f"{process.priority}"
            )

        self.console.print(self.table)
        sum_of_waiting_time = sum([process.waiting_time for process in processes])
        sum_of_turnaround_time = sum([process.turnaround_time for process in processes])

        print(f"Average waiting time: {sum_of_waiting_time / len(processes)}")
        print(f"Average turnaround time: {sum_of_turnaround_time / len(processes)}")

    def FCFS(self):
        processes = []
        n = int(input("Enter the number of processes: "))
        for i in range(0, n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))

            processes.append(Process(i + 1, arrival_time=at, burst_time=burst_time))

        processes.sort(key=attrgetter("arrival_time"))

        time = 0
        for i in processes:
            i.completion_time = (i.arrival_time + i.burst_time) + time
            i.turnaround_time = i.completion_time - i.arrival_time
            i.waiting_time = i.turnaround_time - i.burst_time
            time = i.completion_time

        self.draw(processes)

    def RR_beta(self):

        ready_stack = []
        runing_stack = []
        processes = []
        processes3 = []
        processes2 = []

        n = int(input("Enter the number of processes: "))
        for i in range(0, n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))

            processes.append(Process(i + 1, arrival_time=at, burst_time=burst_time))
            processes2.append(Process(i + 1, arrival_time=at, burst_time=burst_time))
        TQ = int(input("Enter the Time Quantum: "))
        processes.sort(key=attrgetter("arrival_time"))
        processes2.sort(key=attrgetter("arrival_time"))

        time_spent = processes[0].arrival_time
        index = -1
        while True:
            if len(processes2) == 0:
                break
            for i in processes2:
                if i.arrival_time <= time_spent and i not in ready_stack and i not in processes3:
                    ready_stack.append(i)
                    # print("-----------------------Adding in ready stack--------------------------------")
                    # print(f"READY STACK {[i.pid for i in ready_stack]}")
                    # print(f"Process3 STACK {[i.pid for i in processes3]}")

            for r in runing_stack:
                ready_stack.append(r)

            # if len(ready_stack) >1:
            #      if ready_stack[0] == ready_stack[-1]:
            #         ready_stack.pop(0)

            ready_stack = ready_stack[index + 1:]
            # print(f"Ready stack after slicing {[c.pid for c in ready_stack]}")

            # print("-----------------------Before--------------------------------")
            # print(f"READY STACK {[i.pid for i in ready_stack]}")
            # print(f"RUNNING STACK {[i.pid for i in runing_stack]}")
            # print(f"PROCESS2 STACK {[i.pid for i in processes2]}")
            runing_stack = []

            for index, i in enumerate(ready_stack):
                if len(processes2) == 0:
                    break

                print(f"\nNOW RUNNING {i.pid}\n")

                if True:

                    if i.burst_time > TQ:
                        i.burst_time -= TQ
                        runing_stack.append(i)
                        time_spent += TQ

                        # try:
                        #     a = ready_stack.pop(0)
                        #     print(f"Popping the first element from ready stack {a.pid}")
                        #     print(f"Ready stack after popping {[c.pid for c in ready_stack]}")
                        # except:
                        #     pass


                    else:
                        runing_stack.append(i)

                        time_spent += i.burst_time
                        i.completion_time = time_spent
                        # print(f"Removing process {i.pid} having completion time {i.completion_time}")
                        processes3.append(i)
                        processes2.remove(i)

                        runing_stack = [value for value in runing_stack if value != i]
                        # ready_stack = [value for value in ready_stack if value != i]

                        # print("-----------------------After--------------------------------")
                        # print(f"READY STACK {[i.pid for i in ready_stack]}")
                        # print(f"RUNNING STACK {[i.pid for i in runing_stack]}")
                        # print(f"PROCESS2 STACK {[i.pid for i in processes2]}")

        for i in processes3:
            for j in processes:
                if j.pid == i.pid:
                    i.burst_time = j.burst_time
                    # print(f"P {[(c.pid,c.burst_time) for c in processes]}")
                    # print(f"P3 {[(c.pid,c.burst_time) for c in processes3]}")
                    break
            i.turnaround_time = i.completion_time - i.arrival_time
            i.waiting_time = abs(i.turnaround_time - i.burst_time)
        self.draw(processes3)


if __name__ == "__main__":
    obj = Algorithems()
    # obj.priority_pre_beta() #https://www.geeksforgeeks.org/preemptive-priority-cpu-scheduling-algortithm/
    # obj.FCFS()
    # obj.SJF_pre_beta() #https://prepinsta.com/operating-systems/shortest-job-first-scheduling-preemptive-example/#:~:text=SJF%20Preemptive%20Example&text=It's%20the%20only%20process%20so,and%20P2%20process%20starts%20executing.
    # https://www.tutorialandexample.com/shortest-job-first-sjf-scheduling
    # obj.SJF_beta()
    # obj.RR_beta() #https://www.gatevidyalay.com/round-robin-round-robin-scheduling-examples/
    obj.priority_beta()  # https://www.javatpoint.com/os-non-preemptive-priority-scheduling#:~:text=In%20the%20Non%20Preemptive%20Priority,the%20priority%20of%20the%20process.


