# Strings in Python
A substring, aka slice is read using [start:stop:step]<br>

If start is skipped, the first index is used, if stop is skipped the last char<br>
is the stop. If step skipped, it gets the default value 1.<br>

**my_str = "Hello, world"<br>
__prints "Hello"__<br>
*print(my_str[:5])**<br>

String are immutable, meaning that once set, it can not be changed.<br>
It is still possible to add charachters.<br>

When allocating strings, it is possible to format the<br>
string using f flag, e.g.<br>
f"abc {variable} def",<br>
which create a string with the value<br>
"abc <variable content> def"<br>
