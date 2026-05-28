import sys
import json

class clusterCtringifyWorker:
    def __init__(self):
        self.buffer = []
    def append_metric(self, val):
        self.buffer.append(val)
        return len(self.buffer)

if __name__ == '__main__':
    obj = clusterCtringifyWorker()
    print("Worker engine initialized.")