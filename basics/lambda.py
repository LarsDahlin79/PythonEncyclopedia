

def my_sorting_func(event):
    return event[1]

def main():
    # Not the indented why to use lambda functions, just showing syntax
    increment = lambda x : x + 1
    print(f"{increment(10)=}")
    print(f"{increment(122)=}")
    print(f"{increment(10 + 15)=}")

    my_list = [5,1,2,7,3,9,8,4,6]
    print(f"{my_list=}")
    my_list = sorted(my_list)
    print(f"{my_list=}")
    my_list = [5,1,2,7,3,9,8,4,6]
    print(f"{my_list=}")
    my_list = sorted(my_list, reverse=True)
    print(f"{my_list=}")

    my_list = (("jkl", 190),
               ("abc", 120),
               ("ghi", 100),
               ("def", 170),
               ("mno", 110))
    print("Unsorted function")
    print(f"{my_list}")
    print("Sorting used sorted")
    print(f"{sorted(my_list)}")

    # Sorting using fucntion
    print("Sort using user defined function")
    print(f"{sorted(my_list, key = my_sorting_func)}")

    # Sorting using lambda function, name 
    print("Sort using lambda, name")
    print(f"{sorted(my_list, key = lambda event: event[0])}")

    # Sorting using lambda function, value
    print("Sort using lambda, value")
    print(f"{sorted(my_list, key = lambda event: event[1])}")

if __name__ == "__main__":
    main()
