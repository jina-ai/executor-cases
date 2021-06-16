from jina import Executor, requests
from b import b_func


class MyExecutor(Executor):
    @requests
    def foo(self, **kwargs):
        b_func()
