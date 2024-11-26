from src.process_manager.pglobals import Process, Process_mutables, PRIORITY_CLASS, USER_PRIORITY_CLASS


def init_processes():
    os_process = Process()
    os_process.id = 0
    os_process.name = "Os Academic"
    os_process.next = None
    os_process.previous = None
    os_process.priority_class = PRIORITY_CLASS.NORMAL_PRIORITY
    os_process.user_priority_class = USER_PRIORITY_CLASS.NORMAL_USER_PRIORITY
    os_process.priority = PRIORITY_CLASS.NORMAL_PRIORITY.value * USER_PRIORITY_CLASS.NORMAL_USER_PRIORITY.value
    os_process.current_priority = os_process.priority

    Process_mutables.process_list_head = os_process
    Process_mutables.process_list_tail = os_process
    Process_mutables.process_count += 1

    for i in range(1,11):

        Process_mutables.create_process(str(i))

    Process_mutables.print_processes()