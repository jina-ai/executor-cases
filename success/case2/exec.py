from jina import Executor, requests


class MyExecutor(Executor):

    def __init__(self, bar):
        super().__init__()
        self.bar = bar

    @requests
    def foo(self):
        pass
