from services.manager import NoteManager

def show_menu():
    print("\n=== Simple Note App ===")
    print("1. Create a note")
    print("2. View all notes")
    print("3. Read a note")
    print("4. Delete a note")
    print("5. Exit")


def main():

    while True:
        manager = NoteManager()
        show_menu()
        choice = input("Choose an option 1-5: ")
        if choice == "1":
            title = input("Enter the note title: ")
            content = input("Enter the Note:\n")
            manager.create_note(title, content)
        elif choice == "2":
            manager.list_notes()
        elif choice == "3":
            title = input("Enter the note title: ")
            manager.read_note(title)
        elif choice == "4":
            title = input("Enter the note title: ")
            manager.delete_note(title)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Please enter a valid choice!....")

if __name__ == "__main__":
    main()