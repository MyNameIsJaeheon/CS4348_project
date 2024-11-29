import os
import struct

HEADER_SIZE = 512
MAGIC_NUMBER = b"4337PRJ3"

class IndexFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.header = None

    def create(self, overwrite=False):
        if os.path.exists(self.filename) and not overwrite:
            print("File exists. Overwrite? (yes/no)")
            return
        with open(self.filename, "wb") as f:
            # Write header
            f.write(MAGIC_NUMBER)
            f.write((0).to_bytes(8, 'big'))  # Root ID
            f.write((1).to_bytes(8, 'big'))  # Next Block ID
            f.write(b'\x00' * (HEADER_SIZE - 24))  # Padding
        print(f"File {self.filename} created.")

    def open(self):
        if not os.path.exists(self.filename):
            print("File does not exist.")
            return
        with open(self.filename, "rb") as f:
            magic = f.read(8)
            if magic != MAGIC_NUMBER:
                print("Invalid file.")
                return
            self.header = f.read(HEADER_SIZE - 8)
        print(f"File {self.filename} opened.")

# Interactive Menu
def main():
    index_file = None
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "create":
            filename = input("Enter filename: ")
            overwrite = input("Overwrite? (yes/no): ").strip().lower() == "yes"
            index_file = IndexFile(filename)
            index_file.create(overwrite)
        elif command == "open":
            filename = input("Enter filename: ")
            index_file = IndexFile(filename)
            index_file.open()
        elif command == "quit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
