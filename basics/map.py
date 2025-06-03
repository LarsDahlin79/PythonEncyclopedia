

def main():
    int_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]
    print("Starting list")
    for value in int_list:
        print(f"{value}", end = " ")
    print()
    print()

    updated_list = map(lambda x : x * 2, int_list)
    # Type is "map"
    print(f"{type(updated_list)=}")
    print("Updated list")
    for value in updated_list:
        print(f"{value}", end = " ")
    print()
    print()

if __name__ == "__main__":
    main()
