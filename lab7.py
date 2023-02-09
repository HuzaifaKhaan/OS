# threading
import threading
def name_fun(name):
    print(f"hello studentName{name}")
def roll_fun(roll):
    print(f"student roll no is",roll)


t1 = threading.Thread(target=name_fun,args=("iwa",))
t2 = threading.Thread(target=roll_fun,args=(1,));
t1.start()
t2.start()
t2.join()
t2.join()


# task 2

def create_tr(n):
    print(f"hello \n thread number : {n}")


n = int(input("enter no of thread :  "))
thread_li = []
for i in range(n):
    t1 =threading.Thread(target=create_tr,args = (i,))
    t1.start()
    thread_li.append(t1)

for i in thread_li:
    i.join()