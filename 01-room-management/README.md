# 01 - Rooms Management

This project is part of my professional portfolio at **Codelearn**, developed to support personalized tutoring for university-level students. It simulates a simple hotel room and reservation management system using Python, file handling, and modular design.

## 🎯 Project Goal

To create a command-line tool that allows a hotel to manage room availability, reservations, and customer data persistently using `.txt` files.

The project follows academic constraints such as:
- Mandatory use of functions and modules.
- No use of infinite loops or advanced concepts not taught in class.
- No graphical interface; all actions are performed via command-line arguments.

## 🧠 Features

- Add, list, and update room information.
- Handle room states: available, occupied, dirty.
- Manage client reservations.
- Finalize stays and calculate total price.
- Store all data persistently in plain text files.

## 🔧 Technologies Used

- Python 3
- File I/O (`open()`, `read()`, `write()`)
- Modular programming
- Command-line argument parsing (`sys.argv`)
- Git & GitHub

## 📁 Structure

01-rooms-managemens/ ├── main.py # Entry point for command execution. ├── habitacions.py # Room management logic. ├── reserves.py # Reservation logic. ├── fitxers.py # File handling utility functions (planned) ├── dades/ │ ├── habitacions.txt # Stores room data │ └── reserves.txt # Stores reservation data. └── README.md # Project overview


## 📌 Note

This project was developed as part of a university assignment simulation. It reflects the kind of tutoring and support provided to students through custom-developed code examples and technical guidance.
