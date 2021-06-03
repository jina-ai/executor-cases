from jina import Executor, requests

from jinacommon.dep import hello


class MyExecutor2(Executor):
    def __init__(self, bar):
        super().__init__()
        self.bar = bar

    @requests
    def foo(self):
        hello()
