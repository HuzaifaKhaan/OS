import sys
from multiprocessing import Process, Pipe

def parent(conn,name):
    print("parent")
    conn.send(name)
    conn.close()


def child(conn):
    print("child")
    print(conn.recv())
    conn.close()

name = sys.argv[0]
p_comm, c_conn = Pipe()
p = Process(target =parent,args = (p_comm,name,))
c = Process(target =child,args = (c_conn,))

p.start()
c.start()

p.join()
c.join()