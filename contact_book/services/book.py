from models.contact import Contact

class ContactBook:
    def __init__(self):
        self.contacts = []
        
        
    def add_contact(self, name: str, phone: str, email: str):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to show")
        else:
            print("Contacts List:")
            for contact in self.contacts:
                print(contact)
    
    def search_contact(self, name: str):
        found = False
        for contact in self.contacts:
            if contact.name == name:
                print("contact fount=>", contact)
                found = True
        if not found:
            print("Contact not found!")