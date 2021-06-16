from a import a_func
import c


def b_func():
    a_func()
    print("this is func in B module")
    c.c_func()
