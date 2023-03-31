import sys

# print("hello " , "my name is" , sys.argv[1] , "and I am" , sys.argv[2] , "years old")


# It will print the name of the file with no arguments
# print("hello" , "my name is" , sys.argv[0])

# Handling the error if the user does not enter the arguments
# try:
#     print("hello" , "my name is" , sys.argv[1] , "and I am" , sys.argv[2] , "years old")
# except IndexError:
#     print("Please enter the arguments")

# Handling the error if the user enters the wrong arguments
if len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few arguments")

print("hello", "my name is", sys.argv[1], "and I am", sys.argv[2], "years old")
