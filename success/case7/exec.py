from jina import Executor, requests
import numpy as np
from dep import hello


class MyExecutor(Executor):

    def __init__(self, bar, **kwargs):
        super().__init__(**kwargs)
        self.bar = bar

    @requests
    def foo(self, **kwargs):
        hello()
        print(np.__version__)
