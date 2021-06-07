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

if __name__ == '__main__':
    ex =MyExecutor(bar=1)
    ex.foo()