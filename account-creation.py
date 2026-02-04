import sqlite3
import hashlib
from getpass import getpass

# ---- Creating the hash_password function ----


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---- Creating an account ----

username = input("Choose a username: ")

while True:
    password = getpass("Choose a password: ")
    password_verification = getpass("Repeat you password: ")

    if password == password_verification:
        break
    else:
        print("The passwords do not match. Try again.")

# ---- Saving the account to the backend/database ----

conn = sqlite3.connect("database/accounts.db")
cursor = conn.cursor()

try:
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, hash_password(password)),
    )
    conn.commit()
    print(f"Your account ({username}) got saved!")
except sqlite3.IntegrityError:
    print("The account already exists!")

conn.close()
