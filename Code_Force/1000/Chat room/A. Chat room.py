def is_hello(s):
    hello = "hello"
    hello_index = 0

    for char in s:
        if char == hello[hello_index]:
            hello_index += 1
            if hello_index == len(hello):
                return "YES"
    return "NO"


# Custom input
custom_input = input()
print(is_hello(custom_input))
