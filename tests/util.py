from typing import Callable, TypeVar
from functools import wraps

# Define type-variable for test-function return-type
T = TypeVar('T')


def test(name: str):
    """
    Decorator for unit-test.
    This decorator improves the logging for test-cases.

    :param name:      Name of test-case
    """
    def test_decorator(function: Callable[..., T]):
        @wraps(function)
        def test_wrapper(*args):
            return_value: T = None

            header = f"     {name}     "
            divider = "-" * (len(header) + 10)

            # Log header
            print(divider)
            print(f"     {header}     ")
            print(divider)
            print(f"[Starting]")

            return_value = function(*args)

            # Log footer
            print(f"[Finished]")
            print(divider)
            print()

            return return_value
        return test_wrapper
    return test_decorator
