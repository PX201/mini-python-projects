import os

class NoteManager:
    def __init__(self, notes_dir="notes"):
        self.notes_dir = notes_dir
        os.makedirs(self.notes_dir, exist_ok=True)
    
    def create_note(self, title, content):
        filename = os.path.join(self.notes_dir, f"{title}.txt")
        if os.path.exists(filename):
            print("A note with this title already exists!")
            return
        
        with open(filename, "w") as file:
            file.write(content)
        print(f"Note '{title}' created successfully.")

    def list_notes(self):
        files = os.listdir(self.notes_dir)
        if not files:
            print("No notes found.")
            return
        print("Notes:")
        for file in files:
            print(" -", file.replace(".txt", ""))

    def read_note(self, title):
        filename = os.path.join(self.notes_dir, f"{title}.txt")
        if not os.path.exists(filename):
            print("Note not found!")
        with open(filename, "r") as file:
            content = file.read()
            print(f"\n {title}\n{'-'*30}\n{content}\n{'-'*30}")        
        
    def delete_note(self, title):
        filename = os.path.join(self.notes_dir, f"{title}.txt")
        if not os.path.exists(filename):
            print("File not found!")
        else:
            os.remove(filename)
            print(f"Note {title} deleted successfully!")
    
    

        