from enum import Enum
from problem import Problem

class Message_Code(Enum):
    DISCONNECT = 0
    STRING = 1
    PROBLEM = 2

class Message:
    def __init__(self, msg_type: Message_Code) -> None:
        self.msg_type = msg_type

class Problem_Message(Message):
    def __init__(self, problem: Problem) -> None:
        super().__init__(Message_Code.PROBLEM)
        self.problem = problem

    def get_msg(self) -> Problem:
        return self.problem

class String_Message(Message):
    def __init__(self, msg: str) -> None:
        super().__init__(Message_Code.STRING)
        self.msg = msg

    def get_msg(self) -> str:
        return self.msg

class Disconnect_Message(Message):
    def __init__(self) -> None:
        super().__init__(Message_Code.DISCONNECT)

