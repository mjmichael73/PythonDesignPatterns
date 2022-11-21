import time
from functools import wraps


def profiling_wrapper(f):
    @wraps(f)
    def wrap_f(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        elpased_time = end_time - start_time
        print("[Time elpased for n = {}] {}".format(*args, elpased_time))
        return result
    return wrap_f


def profiling_all_class_methods(Cls):
    class ProfiledClass(object):
        def __init__(self, *args, **kwargs):
            self.inst = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(ProfiledClass, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                x = self.inst.__getattribute__(s)
                if type(x) == type(self.__init__):
                    return profiling_wrapper(x)
                else:
                    return x
    return ProfiledClass


@profiling_all_class_methods
class DoMathStuff(object):
    def __init__(self) -> None:
        pass

    def fib(self, n):
        print("Inside fib")
        if n < 2:
            return
        fibPrev, fib = 1, 1
        for _ in range(2, n):
            fibPrev, fib = fib, fib + fibPrev
        return fib


if __name__ == "__main__":
    my_obj = DoMathStuff()
    print(my_obj.fib(n=88))
