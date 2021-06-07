from jina import Executor, requests


class MyExecutor(Executor):

    @requests
    def foo(self, bar, **kwargs):
        print(f'bar = {bar}')
