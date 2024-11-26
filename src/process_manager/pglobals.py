from __future__ import annotations
from enum import Enum

import random


class PRIORITY_CLASS(Enum):
    REALTIME_PRIORITY = 10.0
    HIGH_PRIORITY = 5.0
    NORMAL_PRIORITY = 3.0
    LOW_PRIORITY = 1.0
    IDLE_PRIORITY = 0.5

class USER_PRIORITY_CLASS(Enum):
    REALTIME_USER_PRIORITY = 2.5
    HIGH_USER_PRIORITY = 2.0
    NORMAL_USER_PRIORITY = 1.5
    LOW_USER_PRIORITY = 1.0
    IDLE_USER_PRIORITY = 0.5



class Process:
    id: int
    pid: int
    name: str

    priority_class: PRIORITY_CLASS
    user_priority_class: USER_PRIORITY_CLASS
    priority: float
    current_priority: float

    next: Process
    previous: Process

    last_time_cpu: float

    pc: int = 0


class Process_mutables:
    process_list_head: Process = None
    process_list_tail: Process = None
    process_count: int = 0

    current_process: Process = None

    def add_process(process: Process):
        head = Process_mutables.process_list_head

        if process.priority > head.priority:
                Process_mutables.process_list_head.previous = process
                process.next = Process_mutables.process_list_head
                Process_mutables.process_list_head = process
                Process_mutables.process_count += 1

        while head.next:
            if process.priority > head.next.priority:
                process.next = head.next
                head.next.previous = process
                head.next = process
                process.previous = head
                return 1
            head = head.next

        head.next = process
        process.previous = head
        return 1


    def create_process(name: str, priority_class: PRIORITY_CLASS = PRIORITY_CLASS.NORMAL_PRIORITY):
        process = Process()
        process.id = Process_mutables.process_count
        process.pid = -1
        process.name = name

        process.priority_class = priority_class
        process.user_priority_class = USER_PRIORITY_CLASS.NORMAL_USER_PRIORITY
        process.priority = priority_class.value * USER_PRIORITY_CLASS.NORMAL_USER_PRIORITY.value
        process.current_priority = process.priority

        process.next = None
        process.previous = None

        Process_mutables.add_process(process)


    def print_processes():
        head = Process_mutables.process_list_head
        print(f'Id: {head.id}  |  Name: {head.name}  |  Prio: {head.priority}')
        while head.next:
            head = head.next
            print(f'Id: {head.id}  |  Name: {head.name}  |  Prio: {head.priority}')

    def hugo():
        pass