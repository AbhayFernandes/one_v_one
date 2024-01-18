import socket
import pickle
import os
from enum import Enum
import glob
import threading
from problem import Problem
from messages import Message, Message_Code, String_Message, Problem_Message

HEADER = 64
PORT = 5060
SERVER = "35.11.206.210"
FORMAT = "utf-8"


class Connection:
    def __init__(self, address, app):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((address, PORT))
        # self.thread = threading.Thread(target=self.handle_receive)
        self.app = app

    def padding(self, msg: int) -> str:
        return str(msg).zfill(HEADER)

    def send(self, msg: Message) -> None:
        message = pickle.dumps(msg)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

    def handle_receive(self) -> None:
        connected = True
        while connected:
            msg_length = self.client.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.client.recv(msg_length)
                msg = pickle.loads(msg)
                if msg.msg_type == Message_Code.STRING:
                    print(msg.get_msg())
                elif msg.msg_type == Message_Code.PROBLEM:
                    print("Problem recieved")
                    self.app.set_problem(msg.get_msg())
                    print(f"Problem recieved {msg.get_msg()}")
                elif msg.msg_type == Message_Code.DISCONNECT:
                    connected = False
                else:
                    print(f"Unknown message type: {msg.msg_type}")

    def disconnect(self) -> None:
        pass

class Application:
    def __init__(self, path):
        self.PATH = path
        for f in glob.glob(f"{path}/*"):
            os.remove(f)
        self.CONNECTION = Connection(SERVER, self)
        self.problem = None

    def set_problem(self, problem):
        if not self.problem:
            self.problem = problem
            self.problem.write_problems(self.PATH)

    def get_connection(self):
        return self.CONNECTION

if __name__ == "__main__":
    print(f"Please input the directory where VSCode is open.")
    PATH = input()
    app = Application(PATH)
    app.get_connection().handle_receive()
    # app.run()


