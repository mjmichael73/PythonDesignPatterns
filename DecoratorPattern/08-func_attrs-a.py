def dummy_decorator(f):
    def wrap_f():
        print("Function to be decorated: ", f.__name__)
        print("Nested wrapping function: ", wrap_f.__name__)
        return f()
    return wrap_f

@dummy_decorator
def do_nothing():
    print("Inside do_nothing")

if __name__ == "__main__":
    print("Wrapped function: ", do_nothing.__name__)
    do_nothing()