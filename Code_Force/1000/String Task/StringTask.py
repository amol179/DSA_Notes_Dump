def process_string(s):
    vowels = "aoyeuiAOYEUI"
    result = ""
    for char in s:
        if char not in vowels:
            result += "." + char.lower()
    return result


# Take input from the user
input_string = input()
processed_string = process_string(input_string)
print(processed_string)
