from jina import Executor, requests


class MyExecutor(Executor):

    def __init__(self, bar, **kwargs):
        super().__init__(**kwargs)
        self.bar = bar

    @requests
    def foo(self, **kwargs):
        pass
