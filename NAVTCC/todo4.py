import re

def valid_name(name):
    name_pattern = r'^[a-zA-Z]+\s+[a-zA-z]+'
    name_match = re.match(name_pattern, name)
    return name_match
def valid_phone(phone):
    phone_pattern = r'^[0-9]{4}\-[0-9]{7}'
    phone_match = re.match(phone_pattern, phone)
    return phone_match
def valid_mail(email):
    email_pattern = r'^[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-zA-Z]'
    email_match = re.match(email_pattern, email)
    return email_match
def add_contact(data):
    # Get the contact from the user
    while True:
        name = input("Enter Full Name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        name_val = valid_name(name)
        phone_val = valid_phone(phone)
        email_val = valid_mail(email)

        if email_val and phone_val and name_val:
            data[name] = {'phone': phone, 'email': email}
            print("Contact added successfully!")
            break
        elif not name_val:
            print("Please enter Full Name e.g(John linkon)")
        elif not phone_val:
            print("Please enter correct phone number (0xxx-xxxxxxx)")
        elif not email_val:
            print("Please enter valid email address")
        elif not name_val and not phone_val:
            print("Please enter Full Name and valid Phone Number")
        elif not name_val and not email_val:
            print("Please enter Full Name and valid Email Address")
        elif not email_val and not phone_val:
            print("Please enter valid Email Address and Phone Number")
        else:
            print("Please enter Full Name and valid Email and Phone Number")

def remove_contact(data):
    while True:
        name = input("Enter Full Name: ")
        name_val = valid_name(name)
        if name_val:
            if name in data:
                del data[name]
                print(f"Contact named {name} removed successfully!")
                break
            else:
                print(f"No contact named {name} found")
                break
        else:
            print("Please enter Full Name e.g(John linkon)")



def search_contact(data):
    while True:
        print("How would you like to search contact:\n1: By Name\n2: By Phone Number\n3: By Email Address\n4: Show Menu")
        choice = int(input("Enter your selection: "))
        
        if choice == 1:
            name = "Shahzaib Hassan"  # Predefined value for testing
            name_val = valid_name(name)
            if name_val:
                if name in data.keys():
                    phone, mail = data[name]['phone'], data[name]['email']
                    print(f"Name: {name}\nPhone: {phone}\nEmail: {mail}")
                else:
                    print(f"No contact named {name} found")
                break
            else:
                print("Please enter Full Name e.g(John linkon)")
        elif choice == 2:
            phone = "0302-7701345"  # Predefined value for testing
            phone_val = valid_phone(phone)
            if phone_val:
                found = False
                for name, contact in data.items():
                    if phone == contact['phone']:
                        print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
                        found = True
                if not found:
                    print(f"No contact with phone number {phone} found")
                break
            else:
                print("Please enter correct phone number (0xxx-xxxxxxx)")    
        elif choice == 3:
            email = "shahxeebhassan@Gmail.com"  # Predefined value for testing
            email_val = valid_mail(email)
            if email_val:
                found = False
                for name, contact in data.items():
                    if email == contact['email']:
                        print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
                        found = True
                if not found:
                    print(f"No contact with email address {email} found")
                break
            else:
                print("Please enter valid email address")
        elif choice == 4:
            break
        else:
            print("Invalid Choice")


def show_contacts(data):
    for name, contact in data.items():
        print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")
def show_menu():
    print("1: Add Contact\n2: Remove Contact\n3: Search Contact\n4: Show All Contacts\n5: Exit")
    choice = int(input("Enter your selection: "))
    return choice
def main():
    data = {}
    while True:
        choice = show_menu()
        if choice == 1:
            add_contact(data)
        elif choice == 2:
            remove_contact(data)
        elif choice == 3:
            search_contact(data)
        elif choice == 4:
            show_contacts(data)
        elif choice == 5:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
    