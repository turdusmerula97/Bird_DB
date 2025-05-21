# Bird Database Web App

This is a simple Flask web application that manages a database of birds. It uses SQLite to store bird information and allows users to:

- View the list of birds
- Add new birds (with name, description, and average weight)
- Edit or delete birds
- Search for birds by name
- Sort the list by name or average weight

## Project Structure
![Image](https://github.com/user-attachments/assets/1cbd54da-a18c-4ce4-8cb7-a6b11cfeb1b0)

## Installation steps

### 1. Install Python

Make sure Python 3 is installed. You can download it from [python.org](https://www.python.org/downloads/).

Check installation:

```bash
python --version
```

### 2. Create a Virtual Environment
In the project folder:

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Required Packages
With the virtual environment activated:

```bash
pip install -r requirements.txt
```

### 4. Run the App
Run:

```bash
python app.py
```

Open your browser and visit:

```cpp
http://127.0.0.1:5000/
```

## Screenshots

Empty database:

![Image](https://github.com/user-attachments/assets/fbe6e924-a345-49c0-8323-4aafa438d34a)

Filled database:

![Image](https://github.com/user-attachments/assets/3b785c5a-4345-47a4-bf36-2ad178e5cd82)

Sorting by name or weight:

![Image](https://github.com/user-attachments/assets/346b4954-2fbe-4734-9048-b11addc414b7)

Editing or deleting content:

![Image](https://github.com/user-attachments/assets/f35efb14-63c0-4bce-b3cf-f0719259124b)

Searching through the database:

![Image](https://github.com/user-attachments/assets/1494cbea-aa4e-47be-bd7f-ec2cc16c5f39)
