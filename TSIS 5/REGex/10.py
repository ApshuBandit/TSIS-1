import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case


camel_case_string = "ConvertThisCamelCaseStringToSnakeCase"
snake_case_string = camel_to_snake(camel_case_string)
print("Camel case:", camel_case_string)
print("Snake case:", snake_case_string)
