import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def write_log(message):
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message + '\n')
                else:
                    print(message)

            func_name = func.__name__
            write_log(f"Начало выполнения функции '{func_name}'")
            try:
                result = func(*args, **kwargs)
                write_log(f"Функция '{func_name}' успешно завершена. Результат: {result}")
                return result
            except Exception as e:
                args_repr = [repr(a) for a in args]
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
                all_args = ", ".join(args_repr + kwargs_repr)
                error_type = type(e).__name__
                write_log(f"Функция '{func_name}' вызвала ошибку {error_type}. "
                          f"Аргументы: {all_args}. Ошибка: {e}")
                raise
        return wrapper
    return decorator
