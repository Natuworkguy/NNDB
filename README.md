# NNDB - Nathan Network DataBase

**NNDB** (Nathan Network DataBase) is a lightweight, terminal-friendly database emulator written in Python. It provides an in-memory data store and an interactive shell interface (**DBSH**) for managing data efficiently from the terminal.

---

## Features

- Simple and fast in-memory database.
- Easy to use with context manager support.
- Built-in shell (`DBSH`) for command-line interaction.
- Colored terminal output using `colorama`.
- No third-party database dependencies.

---

## Installation

NNDB is **not available on pip**.

To get started:

1. **Clone the repository:**

```bash
git clone https://github.com/Natuworkguy/nndb.git
cd nndb
```

2. **Install the required dependency:**

```bash
pip install colorama
```

3. **Use `nndb.py` as a module** in your Python scripts.

---

## Quick Start

### Creating and Using a Database

```python
from nndb import DataBase

with DataBase("MyDB") as db:
    db.adddatafrom({"username": "alice", "password": "12345"})
```

### Using the DBSH Shell

```python
from nndb import DataBase, DBSH

db = DataBase("MyDB")
shell = DBSH(db)
shell.run()
```

---

## DBSH Shell Commands

| Command                | Description                                |
|------------------------|--------------------------------------------|
| `hive create <KEY>`    | Create a new key (hive).                   |
| `hive edit <KEY> <VAL>`| Edit or add a value to a key.              |
| `hive show <KEY>`      | Display the value stored at a key.         |
| `hive delete <KEY>`    | Remove a key from the database.            |
| `print <text>`         | Print text to the terminal.                |
| `clear`                | Clear the terminal screen.                 |
| `Get-File <filepath>`  | Display the contents of a file.            |
| `help`, `?`            | Show all available commands.               |
| `exit`                 | Exit the DBSH shell and save changes.      |

---

## Example Session

```
DataBase: MyDB > hive create name
DataBase: MyDB > hive edit name Natuworkguy
DataBase: MyDB > hive show name
Natuworkguy
DataBase: MyDB > exit
```

---

## Requirements

- Python 3.6+
- `colorama` (for terminal coloring)

---

## Notes

- This script is designed to be **imported as a module**, not executed directly.
- Changes in DBSH are synced back to the linked `DataBase` instance on exit.

---

## License

MIT License  
Developed by [Natuworkguy](https://github.com/Natuworkguy)
