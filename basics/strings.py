
def main():
    my_str = "Hello, world"

    # prints "Hello"
    print(my_str[:5])

    # prints "lo"
    print(my_str[2:8:2])

    # print "dlrow ,olleH"
    print(my_str[::-1])

    #print " ,ol"
    print(my_str[6:2:-1])

    # TypeError: 'str' object does not support item assignment
    #my_str[4] = 'x'

    # print len(my_str)=12
    # f means format in this context
    print(f"{len(my_str)=}")
    other_str = f"abc {my_str} def"

    #print "abc Hello, world def"
    print(other_str)

    # A string constant can start and end with either single or double quote
    print("Hello, world")
    print('Hello, world')

    # A string constant start with double quotes can contain single quotes
    # print Hello, 'world'
    print("Hello, 'world'")

    # And vice versa
    # print Hello, "world"
    print('Hello, "world"')

    # Multiline strings
    long_string = """This is a
very long string, too long
too keep it on one line
"""
    print(long_string)

    long_string = '''This is a
very long string, too long
too keep it on one line
'''
    print(long_string)

    # Length of a string
    # print len(my_str)=12
    print(f"{len(my_str)=}")

    # Search for substring
    print(f"{'Hello' in my_str=}")
    print(f"{'Error' in my_str=}")

    # Remove leading and trailing spaces
    print(f"{'    I am Error      '.strip()=}")

    # Convert to upper case
    print(f"{'Hello, world'.upper()=}")

    # Convert to lower case
    print(f"{'Hello, world'.lower()=}")

    # Replace substring
    print(f"{'Hello, world'.replace('world', 'Sweden')=}")

    # Divide a string into array of strings
    print(f'{"Hello, world".split(" ")=}')

    # Concatenating strings
    print("Hello, " + "world")

if __name__ == "__main__":
    main()
