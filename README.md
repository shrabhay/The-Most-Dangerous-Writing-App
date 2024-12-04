# The Most Dangerous Writing App
A simple GUI application that automatically deletes text after a period of user inactivity. Built using Python and the Tkinter library, the app also provides features to save the text before deletion, restart the process, and customize the inactivity timer.

---

## Features
### Text Auto-Deletion
Deletes the content of the text box after a user-defined period of inactivity.

### Customizable Timer
Users can specify the inactivity period (in seconds) after which the text is deleted.

### Save Text Locally
Provides an option to save the text to a file on the local machine before it gets deleted.

### Restart Functionality
Users can restart the process, clearing the text box and resetting the timer.

### Dynamic Window Size
Window dimensions are customizable for better usability.

---

## Prerequisites
* Python 3.6 or higher
* `tkinter` module (comes pre-installed with Python)

---

## Installation
1. Clone the repository:
    ```commandline
    git clone https://github.com/shrabhay/The-Most-Dangerous-Writing-App.git
    cd The-Most-Dangerous-Writing-App
    ```

2. (Optional) Create and activate a virtual environment:
    ```commandline
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies (if any; Tkinter is pre-installed in Python)

---

## Usage
1. Run the application:
    ```commandline
    python3 most_dangerous_writing_app.py
    ```

2. Key Features:

   * Type in the text box.
   * Set the inactivity timer in the input field and press any key to start the timer.
   * Use the Save Text button to save your written content before it is deleted.
   * Use the Restart button to clear the text box and reset the process.

---

## Project Structure
```commandline
AutoDeleteTextApp/
├── auto_delete_app.py   # Main application script
├── README.md            # Project documentation
└── .gitignore           # Files to ignore in Git
```

---

## Contribution
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
    ```commandline
    git checkout -b feature-name
    ```

3. Commit your changes:
    ```commandline
    git commit -m "Add your message here"
    ```

4. Push to the branch:
    ```commandline
    git push origin feature-name
    ```

5. Create a pull request.

---

## License
This project is licensed under the MIT License.