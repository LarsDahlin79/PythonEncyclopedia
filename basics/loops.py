

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
    # If break is used to exit the loop, else statements is not executed
    for it in range(5):
        print(it)
    else:
        print("Loop is over")

    # Allocating a list using for
    my_list = [x*x for x in range(5)]
    print(my_list)

    # Modifying iterator in a for loop
    # This will print the value "5" 5 times
    for it in range(5):
        it = 5
        print(it)

    # while loops executes until condition is false
    it = 0
    while it < 5:
        print(it)
        it += 1

    # while can also include else, which is executed after the last iteration
    it = 0
    while it < 5:
        print(it)
        it += 1
    else:
        print("End of while loop")

    # break and continue works like with for loops

if __name__ == "__main__":
    main()
