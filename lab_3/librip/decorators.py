def print_result(func_to_decorate):
    def decorated_func(*args, **kwargs):
        print(func_to_decorate.__name__)
        if type(func_to_decorate(*args, **kwargs)) == list:
            for i in func_to_decorate(*args, **kwargs):
                print(i)
            return func_to_decorate(*args, **kwargs)
        elif type(func_to_decorate(*args, **kwargs)) == dict:
            for i in func_to_decorate(*args, **kwargs).keys():
                print('{} = {}'.format(i, func_to_decorate(*args, **kwargs)[i]))
        else:
            print(func_to_decorate(*args, **kwargs))

    return decorated_func
