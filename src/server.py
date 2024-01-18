import socket
import urwid
import threading
from enum import Enum
import pickle
from problem import Problem
from messages import Message, Message_Code, String_Message, Problem_Message


HEADER = 64
PORT = 5060


class Server:
    HEADER = HEADER 
    PORT = PORT 
    IP = socket.gethostbyname(socket.gethostname())
    ADDR = (IP, PORT)
    FORMAT = "utf-8"
    DISCONNECT_MESSAGE = "!DISCONNECT"

    def __init__(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.clients = []

    def start(self): 
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.IP}")
        thread = threading.Thread(target=self.handle_connections)
        thread.start()
        print(f"Enter y to send a problem")
        if input() == "y":
            self.send_problem()

    def handle_connections(self):
        while True:
            conn, addr = self.server.accept()
            self.clients.append(Client(conn, addr))
            thread = threading.Thread(target=self.clients[-1].handle, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    def send_problem(self):
        problem = Problem("problems/no_duplicates")
        msg = Problem_Message(problem)
        msg = pickle.dumps(msg)
        msg_len = len(msg)
        msg_len = str(msg_len).encode(self.FORMAT)
        msg_len += b' ' * (self.HEADER - len(msg_len))
        for client in self.clients:
            client.get_conn().send(msg_len)
            client.get_conn().send(msg)


class Client:
    HEADER = HEADER 
    FORMAT = "utf-8"
    DISCONNECT_MESSAGE = "!DISCONNECT"

    def __init__(self, conn, addr) -> None:
        self.CONN = conn
        self.ADDR = addr

    def get_conn(self):
        return self.CONN

    def handle(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")    

        connected = True
        while connected:
            msg_len = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_len:
                msg_len = int(msg_len)
                message = pickle.loads(conn.recv(msg_len))
                if message.msg_type == Message_Code.DISCONNECT:
                    connected = False
                elif message.msg_type == Message_Code.STRING:
                    print(f"[{addr}] [STRING] {message.get_msg()}")
                elif message.msg_type == Message_Code.PROBLEM:
                    print(f"[{addr}] [PROBLEM] {message}")
                else:
                    continue

        conn.close()

    

if __name__ == "__main__":
    server = Server()
    server.start()

