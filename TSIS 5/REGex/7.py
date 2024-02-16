def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case

# Test the function
snake_case_string = "hello_world_how_are_you"
camel_case_string = snake_to_camel(snake_case_string)
print("Snake case:", snake_case_string)
print("Camel case:", camel_case_string)
