# # This is a sample Python code for testing code analysis tools like SonarQube.
# # It contains intentional code issues and code smells.

# def divide_numbers(a, b):
#     if b == 0:
#         print("Division by zero!")
#     return a / b

# def unused_variable():
#     x = 10  # Unused variable

# def unused_function():
#     pass

# def function_with_long_name_to_trigger_naming_convention_warning():
#     pass

# class MyClass:
#     def __init__(self):
#         self.data = [1, 2, 3]
    
#     def access_index_out_of_range(self):
#         print(self.data[5])  # Index out of range

#     def duplicate_method(self):
#         pass

#     def duplicate_method(self):  # Duplicate method
#         pass

# if __name__ == "__main__":
#     unused_variable()
#     unused_function()
#     function_with_long_name_to_trigger_naming_convention_warning()
    
#     a = 10
#     b = 0
#     result = divide_numbers(a, b)

#     my_instance = MyClass()
#     my_instance.access_index_out_of_range()

#     my_instance.duplicate_method()
