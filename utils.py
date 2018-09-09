def show_docstring_for_method(method, pointer, *args, **kwargs):
    print(input(method.__doc__))

    return pointer(method, *args, **kwargs)
