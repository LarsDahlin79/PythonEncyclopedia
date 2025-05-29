
import math


# Note that in Python exceptions as called errors
class NegativeValueError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def calc_sqrt(value: int) -> int:
    if value < 0:
        raise NegativeValueError("Cannot handle negative values")
    return math.sqrt(value)


def main():

    # How use exceptions in Python
    # Else is executed if no exception was caught
    # finally is executed regardless of exceptions
    # More then one exception can be caught per try statement
    try:
        res = 1 / 0
    except ZeroDivisionError:
        print("Unable to divide by zero")
    except Exception:
        print("General exception")
    else:
        print("No exception happened")
    finally:
        print("End of try-except")

    # How to use custom exceptions
    try:
        sqrt = calc_sqrt(-1)
    except NegativeValueError as exception:
        print(exception)
    else:
        print("No exception happened")
    finally:
        print("End of try-except")

if __name__ == "__main__":
    main()
