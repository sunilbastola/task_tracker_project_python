# Task Tracker CLI

A simple Command Line Interface (CLI) application to manage tasks efficiently. This project allows users to add, update, delete, and track the status of their tasks, storing all data in a JSON file.

## Features
- Add a new task
- Update an existing task
- Delete a task
- Mark tasks as **todo**, **in-progress**, or **done**
- List all tasks or filter by status
- Persistent storage using a JSON file

## Installation
### Clone the Repository
```sh
git clone https://github.com/sunilbastola/task-tracker-cli.git
cd task-tracker-cli
```

### Make the Script Executable
Modify permissions to run the script directly:
```sh
chmod +x main.py
```

### Add to PATH (Optional)
To run the script from anywhere:
```sh
echo 'export PATH="$PATH:$(pwd)"' >> ~/.zshrc  # For zsh users
echo 'export PATH="$PATH:$(pwd)"' >> ~/.bashrc  # For bash users
source ~/.zshrc  # Or source ~/.bashrc
```

## Usage
### Adding a New Task
```sh
python3 main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Updating a Task
```sh
python3 main.py update 1 "Buy groceries and cook dinner"
```

### Deleting a Task
```sh
python3 main.py delete 1
```

### Marking a Task Status
```sh
python3 main.py mark-in-progress 1
python3 main.py mark-done 1
```

### Listing Tasks
#### All Tasks:
```sh
python3 main.py list
```
#### Filter by Status:
```sh
python3 main.py list todo
python3 main.py list in-progress
python3 main.py list done
```

## File Storage
All tasks are stored in a `tasks.json` file in the current directory. The file structure:
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2024-03-27T12:00:00",
    "updatedAt": "2024-03-27T12:00:00"
  }
]
```

## Error Handling
- The script prevents adding empty tasks.
- If a task ID is invalid, an appropriate error message is displayed.
- JSON file errors are handled gracefully.

## License
This project is part of Projects by roadmap.sh.!

## Author
Sunil Bastola

## Contributing
Contributions are welcome! Feel free to submit a pull request.

---

Happy coding! 🚀

