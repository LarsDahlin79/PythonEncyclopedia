
def main():
    my_list = [6, 11, 17, 23, 24, 18]
    print(f"{my_list=}")
    print("(", end = "")
    for value in filter(lambda value : value %2 == 0, my_list):
        print(f"{value}", end = ", ")
    print(")")

    even_values = filter(lambda value : value %2 == 0, my_list)
    print(f"{type(even_values)=}")
    print("(", end = "")
    for value in even_values:
        print(f"{value}", end = ", ")
    print(f")")

if __name__ == "__main__":
    main()
