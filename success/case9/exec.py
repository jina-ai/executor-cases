from jina import Executor, requests
import tensorflow as tf
from dep import hello


class MyExecutor(Executor):

    def __init__(self, bar):
        super().__init__()
        self.bar = bar

    @requests
    def foo(self):
        hello()
        print(tf.__version__)
