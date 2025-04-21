from services.book import ContactBook


def main():
    book = ContactBook()


    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(name, email, phone)
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            name = input("Enter name: ")
            book.search_contact(name)
        elif choice ==  "4":
            print(" Exiting Contact Book. Goodbye!")
            break
        else: 
            print("Invalid entry. Please select 1-4.")

if __name__ == "__main__":
    main()

