from src.process_manager.pglobals import Process


class Core:
    process: Process
    pc: int

    def load(self, process: Process):
        self.process = process
        self.pc = process.pc


class Cores_controller:
    core1: Core = Core()
    core2: Core = Core()
    core3: Core = Core()
    core4: Core = Core()