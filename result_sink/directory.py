from result_sink.sink import Sink

class Directory(Sink):
    def __init__(self, dirname):
        self.dirname = dirname

