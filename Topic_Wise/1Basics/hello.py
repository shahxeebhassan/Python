#print function


name = input("What is your name? ")
print("Hello," , name)
print("Hello, " + name)
print("Hello," ,end=" ")
print(name)
print("Hello," , name , "!",sep="->")
print(f"Hello, {name}!")
#Print double quotes
print('Hello, "Shahzaib"' )
print("Hello, \"Shahzaib\"")

#String functions
Name = input("What is your last name? ").strip().title()
First , Last = Name.split(" ")
print("Hello,"  , First)
print("Hello,"  , Last)

