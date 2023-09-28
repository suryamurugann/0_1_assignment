# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# sample input: 10
# sample output: 35

add = lambda user_input,stand : user_input + stand
print(add(user_input=int(input("Enter Your Input :")),stand=25))
