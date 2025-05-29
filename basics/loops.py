

def main():
    my_str = "Hello, world"
    print(my_str)

    # Prints 0 to 4 (last value is not included
    for it in range(5):
        print(it)

    # As with strings, slices can include start, stop and step
    for it in range(5, 100, 25):
        print(it)

    # Loop through a list
    for it in ["abc", "def", "ghi"]:
        print(it)

    # Exit a for loop
    for it in range(10000):
        print(it)
        if it >= 5:
            break

    # Continue with the next iteration
    # Only prints odd numbers
    for it in range(10):
        if it % 2 == 0:
            continue
        print(it)

    # Else statements run after the loop has ended
    for it in range(5):
        print(it)
    else:
        print("Loop is over")

    # Allocating a list using for
    my_list = [x*x for x in range(5)]
    print(my_list)

if __name__ == "__main__":
    main()
