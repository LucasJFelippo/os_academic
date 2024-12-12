from src.process_manager.pglobals import Process, Process_mutables

def aging():
    head = Process_mutables.process_list_head
    
    while head.next:
        head.next.current_priority += 2.0

def schedule():
    head = Process_mutables.process_list_head

    highest = head

    while head.next:
        pass