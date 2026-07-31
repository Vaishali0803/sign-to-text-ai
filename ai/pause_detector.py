import time


class PauseDetector:

    def __init__(self):

        self.last_time = time.time()

    def update(self):

        self.last_time = time.time()

    def is_pause(self):

        return (time.time() - self.last_time) > 1.5