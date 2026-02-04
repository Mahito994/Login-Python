# Login & Signup Program in Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

This project is a **Login and Signup System**, written in **Python**. It allows users to register and log in, with all user data securely stored in a local **SQLite3 database**.

---

## Features

- **User Registration (Signup)**  
  - Users can create a new account.
  - Passwords are hashed using **`hashlib`** before being stored in the database.

- **User Login**  
  - Authenticate users using stored credentials.
  - Secure password checking using hashes.

- **Database**  
  - Uses **SQLite3** for local storage.
  - All user data is securely hashed and managed locally.

---

## Security

- Passwords are **never stored in plain text**.
- Uses **`hashlib`** to securely hash passwords.
- **SQLite3** ensures local storage of all user data.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mahito994/Login-Python.git

2. Navigate to the project folder:
   ```bash
   cd Login-Python
   
3. Ensure you have Python 3 installed:
   ```bash
   python
   ```
   after that it should show something likt that:
   <br>
   `
   Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   `

4. Exit the python live environment:
   ```bash
   exit()
   ```

   ---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit (`git commit -m 'Add feature'`).
5. Push (`git push origin feature-name`).
6. Open a Pull Request.
