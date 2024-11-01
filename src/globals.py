from __future__ import annotations


class Process:
    id: int
    pid: int
    next: Process
    previous: Process


class Process_mutables:
    process_list_head: Process
    process_list_tail: Process
    process_number: int