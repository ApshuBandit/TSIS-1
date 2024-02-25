

import time
import math



def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Result:", result)  # 120




def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


input_string = input("Vvedite slovo")
upper, lower = count_upper_lower(input_string)
print( upper)  
print( lower)


def is_palindrome(s):
    return s == s[::-1]


input_string = input()
if is_palindrome(input_string):
    print("True")
else:
    print("False")




def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print("Square root of", number, "after", milliseconds, "milliseconds is", result)


square_root_after_milliseconds(25100, 2123)



def all_true(tuple_data):
    return all(tuple_data)


tuple1 = (True, True, True)
tuple2 = (True, False, True)
print(all_true(tuple1))  
print(all_true(tuple2))  