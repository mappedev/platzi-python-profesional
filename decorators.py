from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        inital_time = datetime.now().second
        func(*args, **kwargs)
        final_time = datetime.now().second
        time_elapsed = final_time - inital_time
        print("Pasaron", time_elapsed, "segundos.")

    return wrapper


def with_custom_message(message: str):
    def with_message(func):
        print(message + ":")

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper

    return with_message


@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return a + b


@with_custom_message("Operation")
def multiply(a, b):
    c = a * b
    print(f"Result {a} * {b} is {c}")


def run():
    random_func()
    sum(1, 2)
    multiply(1, 2)


if __name__ == "__main__":
    run()
