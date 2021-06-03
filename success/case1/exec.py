from jina import Executor, requests


class MyExecutor(Executor):

    @requests
    def foo(self, **kwargs):
        pass
