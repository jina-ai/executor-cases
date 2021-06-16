from dep_d.d import d_func
from dep_e import e_func


def c_func():
    print('This is func in C module')
    d_func()
    e_func()
