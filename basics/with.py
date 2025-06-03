
class MyClass:
    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__")


def main():

    print("Before with")
    with MyClass() as obj:
        print(f"{type(obj)=}")
    print("After with")


if __name__ == "__main__":
    main()
