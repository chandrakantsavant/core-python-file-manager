# Python OOP File Manager

A simple command-line file manager built using **Core Python and Object-Oriented Programming (OOP)** concepts.

This project is created as a learning exercise to practice Python classes, methods, file handling, user input, loops, conditional statements, and exception handling.

## Features

The application provides the following options:

1. **Create File**

   * Displays the existing files.
   * Asks the user for a file name.
   * Creates a new file.

2. **Edit File**

   * Displays the existing files.
   * Allows the user to select a file.
   * Allows the user to add or modify file content.

3. **Delete File**

   * Displays the existing files.
   * Allows the user to select a file.
   * Deletes the selected file.

4. **Rename File**

   * Displays the existing files.
   * Allows the user to select a file.
   * Asks for the new file name.
   * Renames the selected file.

5. **Exit**

   * Closes the application.

## Example

```text
=================================
       Python File Manager
=================================

1. Create File
2. Edit File
3. Delete File
4. Rename File
5. Exit

Enter your choice: 1

Existing Files:
----------------
1. test.txt
2. notes.txt
3. demo.txt

Enter new file name: python.txt

File created successfully!

=================================
       Python File Manager
=================================

1. Create File
2. Edit File
3. Delete File
4. Rename File
5. Exit

Enter your choice:
```

## Project Structure

```text
python-oop-file-manager/
│
├── main.py
├── file_manager.py
├── files/
│   └── .gitkeep
│
└── README.md
```

### `main.py`

The entry point of the application.

It creates the `FileManager` object and starts the application.

### `file_manager.py`

Contains the `FileManager` class and its methods for:

* Creating files
* Editing files
* Deleting files
* Renaming files
* Listing files
* Displaying the menu

### `files/`

This directory is used to store the files created by the application.

## OOP Concepts Practiced

This project focuses on the following Python concepts:

* Classes
* Objects
* Constructors
* Instance methods
* Encapsulation
* `self`
* Conditional statements
* Loops
* Functions
* User input
* Exception handling
* File handling
* Working with directories
* OS/file system operations

## Python Concepts

The project uses Core Python without external frameworks or libraries.

Main modules:

```python
os
```

The `os` module is used for file and directory operations such as:

* Listing files
* Creating files
* Deleting files
* Renaming files

## Requirements

Python **3.x**

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

No external packages are required.

## How to Run

Clone the repository:

```bash
git clone https://github.com/<your-username>/python-oop-file-manager.git
```

Move into the project:

```bash
cd python-oop-file-manager
```

Run the application:

```bash
python main.py
```

## Learning Goal

The main goal of this project is to understand how a simple real-world application can be designed using **Object-Oriented Programming in Python**.

The project intentionally starts simple and can be extended later with additional features.

## Future Improvements

Possible future features include:

* Create directories
* Delete directories
* Move files
* Copy files
* Search files
* File size information
* File modification date
* File extensions filtering
* File content preview
* Confirmation before deleting files
* Logging
* Configuration file
* Unit tests
* Better CLI interface

## Author

**Chandrakant Savant**

Learning Python and Object-Oriented Programming.

---

### License

This project is created for learning and educational purposes.
