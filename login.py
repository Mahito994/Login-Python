import sqlite3
import hashlib
from getpass import getpass

# ---- Creating the hash_password function ----


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---- Login system ----

while True:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    conn = sqlite3.connect("database/accounts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))

    row = cursor.fetchone()
    conn.close()

    if row and row[0] == hash_password(password):
        print(f"You logged in as {username} succesfully!")
        break
    else:
        print("Wrong username or password! Try again.")
