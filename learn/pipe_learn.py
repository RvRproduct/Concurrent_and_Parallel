"""
A Pipe() can only have two endpoints.
A Queue() can have multiple producers and consumers.
If you need more than two points to communicate, use a Queue().
If you need absolute performance, a Pipe() is much faster because Queue() is built on top of Pipe().
"""
import multiprocessing as mp
msgs = ["Hey", "Hello", "Hru?", "END"]


def send_msgs(conn, msgs):
    for msg in msgs:
        conn.send(msg)
    conn.close()


def recv_msg(conn):
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print(msg)


if __name__ == "__main__":
    parent_conn, child_conn = mp.Pipe()

    p1 = mp.Process(target=send_msgs, args=(parent_conn, msgs))
    p2 = mp.Process(target=recv_msg, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
