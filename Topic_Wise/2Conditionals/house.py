def main():
    x = input("Enter your Name: ")
    house(x)
    names(x)

def house(z):
    # z.strip();
    if z == "Shahzaib" or z == "Rabia" or z == "Sehrish":
        print("Bahawalpur")
    elif z == "Imran" or z == "Usman":
        print("Ahmadpur")
    else:
        print("Who?")

def names(z):
    match z :
        case "Shahzaib":
            print("Loves Afnan")
        case "Afnan" | "Zara":
            print("Loves Shahzaib")
        case _:
            print("Sorry i've no information about that")
main()