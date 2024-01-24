# Question 1: Take an input string from the user and create a new string with the
# first, middle, and last characters of the input string

#STEPS:
# 1. Take the user input and set it to a variable
# 2. Get the first character using index 0 and store it in a variable
# 3. Get the last character using index -1 and store it in a variable
# 4. To get the middle character, find the length of the string, find the mid index using length/2, get the character at mid index using [mid_index]
# 5. Concatenate a,b,c

user_string = input('Please enter a string: ')
print(user_string)

first_char = user_string[0]
last_char = user_string[-1]

str_length = len(user_string)
mid_index = int(str_length/2) #need to convert to int becayse indices should always be integers

mid_char = user_string[mid_index]

new_str = first_char+mid_char+last_char
print(new_str)