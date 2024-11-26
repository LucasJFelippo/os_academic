from src.sys_clock.clock import clock

from threading import Thread

from src.interrupt_handlers.ihglobals import SysInterrupt_handler

def init_sys_clock():
    clock_thread = Thread(target = clock, args = (SysInterrupt_handler,))
    clock_thread.run()