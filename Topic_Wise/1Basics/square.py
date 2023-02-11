def main():
    num = int(input("Enter a number: "))
    print("Square of", num, "is", square(num))

def square(num):
    return num * num

main()