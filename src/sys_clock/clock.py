from src.interrupt_handlers.ihglobals import SysInterrupt_handler

import time


def clock(handler: SysInterrupt_handler):
    while True:
        time.sleep(5)
        handler.clock_interrupt()