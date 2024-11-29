[2024-11-24]
The project involves creating and managing index files that contain a B-Tree. The program will handle operations such as creating, inserting, searching, and extracting key-value pairs. Key requirements include:

1. Using file-based storage for the B-Tree with a specific format.
2. Handling user interactions and errors robustly.
3. Implementing the B-Tree with minimal memory usage, ensuring no more than three nodes are in memory at any time.
   Plan
4. Set up the repository and devlog.
5. Start with creating the index file and defining the header structure.
6. Implement the menu-driven interface for user commands.
7. Gradually develop the B-Tree logic with serialization and deserialization for file storage.

[2024-11-25]
Focused on setting up the project structure and writing initial code to handle file creation and header management.
Plan

1. Initialize the Git repository and create the devlog.md.
2. Implement the "create" and "open" commands with proper file handling.
3. Write code to validate the header when opening an index file.
   Work Done
   • Created the repository and added the initial devlog entry.
   • Implemented the "create" command to generate a new index file with a proper header.
   • Added logic for the "open" command, including validation of the magic number in the header.
   Challenges
   • Understanding how to write and read binary data using Python’s struct module.
   • Ensuring big-endian format for integers when writing to the file.
   Next Steps
   • Start defining the B-Tree node structure and implement basic file I/O for nodes.

[2024-11-26]
The focus shifted to implementing the B-Tree structure and ensuring its functionality with minimal memory usage.
Plan

1. Define the structure of a B-Tree node in Python, including keys, values, and child pointers.
2. Implement serialization and deserialization of nodes into 512-byte blocks.
3. Begin working on the "insert" command.
   Work Done
   • Defined a Python class for B-Tree nodes with attributes for keys, values, and child pointers.
   • Wrote functions to serialize and deserialize nodes into and from binary format.
   • Implemented a basic "insert" function to add key-value pairs to the tree, including node splitting.
   Challenges
   • Handling edge cases when splitting nodes during insertion.
   • Ensuring the node’s data fits within the 512-byte block limit.
   Next Steps
   • Complete the "insert" functionality and begin implementing the "search" command.

[2024-11-27]
The program now has basic insertion functionality. The focus is on searching the B-Tree and adding features for bulk operations.
Plan

1. Implement the "search" command to locate keys in the B-Tree.
2. Write code for the "load" command to insert key-value pairs from a CSV file.
3. Optimize error handling for invalid inputs and file errors.
   Work Done
   • Implemented the "search" command to traverse the B-Tree and locate keys.
   • Added the "load" command, allowing bulk insertion from a CSV file.
   • Enhanced error handling for missing or invalid input files.
   Challenges
   • Debugging the search functionality to ensure correct traversal through child pointers.
   • Validating the CSV format for bulk insertion.
   Next Steps
   • Implement the "print" and "extract" commands to display and save the B-Tree data.

[2024-11-28]
The project is nearing completion. Focus is on completing the remaining commands and thoroughly testing the program.
Plan

1. Implement the "print" command to display all key-value pairs in the B-Tree.
2. Develop the "extract" command to save the tree data to a file.
3. Test all commands extensively and fix any issues.
   Work Done
   • Wrote the "print" command to display all keys and values in the B-Tree.
   • Developed the "extract" command to export key-value pairs to a CSV file.
   • Fixed bugs in node splitting logic during insertion.
   Challenges
   • Handling overwriting files during extraction gracefully.
   • Ensuring consistent formatting of the exported data.
   Next Steps
   • Conduct full program testing, including edge cases.
   • Write final reflections and prepare the project for submission.

[2024-11-29]
The project is complete, and all commands are functional. Final testing ensured the program meets all specifications.
Plan

1. Perform rigorous testing with various inputs, including empty trees, large datasets, and invalid inputs.
2. Refactor the code to improve readability and add comments/documentation.
3. Make the final Git commit and prepare for submission.
   Work Done
   • Conducted full program testing, fixing minor bugs in the "search" and "load" commands.
   • Cleaned up the code and added comments for clarity.
   • Updated the devlog.md with a detailed summary of progress.
   Challenges
   • None encountered in this session. All planned tasks were completed successfully.
   Final Reflections
   This project provided valuable experience in:
4. Implementing a B-Tree for efficient data storage and retrieval.
5. Handling file-based storage with binary formats.
6. Designing an interactive and user-friendly command-line program.
   The program meets all requirements, and I’m confident it will perform well under evaluation.
