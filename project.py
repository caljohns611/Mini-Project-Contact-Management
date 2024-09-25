contacts = {}

def add_contact(contacts):
    identifier = input("Please enter a phone number or a email: ")
    if identifier in contacts:
        print("Contact already exists.")
        return
    name = input("Enter a name: ")
    phone = input("Enter a phone number: ")
    email = input("Enter a email: ")
    additional_info = input("Enter additioanl information (address, notes, etc.): ")

    contacts[identifier] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info\n": additional_info
    }
    print("\nAdded contact\n")

def edit_contact(contacts):
    identifier = input("Enter a contact you would like to edit: ")
    if identifier not in contacts:
        print("Contact not found")
        return
    name = input("Enter new name (leave blank to keep current): ")
    phone = input("Enter new phone number (leave blank to keep current): ")
    email = input("Enter new email address (leave blank to keep current): ")
    additional_info = input("Enter new additional info (leave blank to keep current): ")

    if name:
        contacts[identifier]["Name"] = name
    if phone:
        contacts[identifier]["Phone"] = phone
    if email:
        contacts[identifier]["Email"] = email
    if additional_info:
        contacts[identifier]["Additional info"] = additional_info
    print("Contact updated")

def delete_contact(contacts):
    identifier = input("Enter a contact you would like to delete: ")
    if identifier in contacts:
        del contacts[identifier]
    else:
        print("Contact not in the list.")

def search_contact(contacts):
    identifier = ("Enter a contact you would like to search: ")
    if identifier in contacts:
        details = contacts[identifier]
        print(f"Identifier: {identifier}")
        print(f"Name: {details['Name']}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
        print(f"Additional info: {details['Additional info']}")
    else:
        print("Contact not in the list.")

def display_contact(contacts):
    if not contacts:
        print("There are no contacts at the moment.")
    else:
        for identifier, details in contacts.items():
            print(f"Identifier: {identifier}, Name: {details['Name']}, Phone: {details['Phone']}, Email: {details['Email']}")

def export_contact(contacts):
    file_name = input("Enter a file to save contacts: ")
    with open (file_name, 'w') as file:
        print(file_name,"\nAdded to file")


def main():
   
    while True:
        print("Welcome to the Contact Management System!\nMenu:")
        print("1. Add a new contact\n2. Edit an exsiting contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quite")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_contact(contacts)
        elif choice == '6':
            export_contact(contacts)
        elif choice == '7':
            break
        else:
            print("Invalid choice try again.")

if __name__=="__main__":
    main()