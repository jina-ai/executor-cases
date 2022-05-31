from jina import Executor, requests

from jinahub.exec1.exec import MyExecutor1


class MyExecutor2(Executor):
    def __init__(self, foo, bar):
        super().__init__()
        self.foo = foo
        self.other_exec = MyExecutor1(bar)

    @requests
    def do_something(self, **kwargs):
        self.other_exec.do_something(**kwargs)
        print(self.foo)
