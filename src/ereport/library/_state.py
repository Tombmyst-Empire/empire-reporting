from datetime import time


class State:
    __run_once: bool = False

    start_time: float = 0.0

    @staticmethod
    def run():
        State.start_time = time()
        State.__run_once = True