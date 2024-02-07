# AirBnB Clone Project

This project is an implementation of a command-line interface (CLI) for a simplified version of the AirBnB platform. It allows users to interact with a set of objects through various commands.

## Command Interpreter

### How to Start
To start the command interpreter, follow these steps:
1. Clone the repository: `git clone https://github.com/username/AirBnB_clone.git`
2. Navigate to the project directory: `cd AirBnB_clone`
3. Run the command interpreter: `./console.py`

### How to Use
Once the command interpreter is running, you can use various commands to interact with the system. Here are some examples of supported commands:
- `create`: Create a new instance of a class.
- `show`: Display information about a specific instance.
- `destroy`: Delete a specific instance.
- `update`: Update attributes of a specific instance.

For a complete list of commands and their usage, type `help` within the command interpreter.

### Examples
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create BaseModel
e7b2d6ad-4bf5-4b1f-af19-88f21f6f16fb
(hbnb) show BaseModel e7b2d6ad-4bf5-4b1f-af19-88f21f6f16fb
[BaseModel] (e7b2d6ad-4bf5-4b1f-af19-88f21f6f16fb) {'id': 'e7b2d6ad-4bf5-4b1f-af19-88f21f6f16fb', 'created_at': '2024-02-07T12:00:00', 'updated_at': '2024-02-07T12:00:00'}
(hbnb) quit

