from jina import Executor, requests


class MyExecutor1(Executor):
    def __init__(self, bar):
        super().__init__()
        self.bar = bar

    @requests
    def do_something(self, **kwargs):
        print(self.bar)
