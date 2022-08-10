from typing import Callable, TypeVar
from functools import wraps

# Define type-variable for test-function return-type
T = TypeVar('T')


def test(name: str, parameter = None):
    """
    Decorator for unit-test.
    This decorator improves the logging and allows for basic parameterized test-cases.

    :param name:      Name of test-case
    :param parameter: [Optional] List of parameter for parameterized test-case
    """
    def test_decorator(function: Callable[..., T]):
        @wraps(function)
        def test_wrapper(*args):
            return_value: T = None

            header = f"{name} {'[PARAMETERIZED]' if parameter else ''}"
            divider = "-" * (len(header) + 10)

            # Log header
            print(divider)
            print(f"     {header}     ")
            print(divider)

            # Parameterized test-case
            if parameter:
                for param in parameter:
                    print(f"[Parameter: {param}]")

                    # Test if `param` consists of multiple values -> iterable
                    try:
                        iter(param)
                    except TypeError:
                        return_value = function(*args, param)       # Single parameter
                    else:
                        return_value = function(*args, *param)      # Multiple parameters

            # Basic test-case
            else:
                return_value = function(*args)

            # Log footer
            print(f"[Finished]")
            print(divider)
            print()

            return return_value
        return test_wrapper
    return test_decorator
