import sqlite3
import hashlib
from getpass import getpass


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


conn = sqlite3.connect("database/accounts.db")
cursor = conn.cursor()

# ---- Creating the sheet ----
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY,
    password_hash TEXT NOT NULL
)
"""
)

# ---- checking if a root password exists ----
cursor.execute("SELECT password_hash FROM admin WHERE id = 1")
root_exists = cursor.fetchone()

# ---- creating the root password ----
if root_exists is None:
    print("No root password found. Please set one.")
    password = getpass("Set root password: ")
    confirm = getpass("Repeat root password: ")

    if password != confirm:
        print("Passwords do not match!")
        conn.close()
        exit(1)

    cursor.execute(
        "INSERT INTO admin (id, password_hash) VALUES (1, ?)",
        (hash_password(password),),
    )
    conn.commit()
    print(f"Root password saved as {password}")
else:
    print("Root password already exists")

conn.close()
