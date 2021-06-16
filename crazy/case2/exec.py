from jina import Executor, requests
from b import b_func
import tensorflow as tf


class MyExecutor(Executor):
    @requests
    def foo(self, **kwargs):
        b_func()
