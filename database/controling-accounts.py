import sqlite3
import sys
import hashlib
from getpass import getpass

# ---- creating the hash_password function ----


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


conn = sqlite3.connect("database/accounts.db")
cursor = conn.cursor()

# ---- getting the permission ----
root_password = getpass("Enter the root-password to continue: ")

cursor.execute("SELECT password_hash FROM admin WHERE id = 1")
result = cursor.fetchone()

if result is None:
    print("No root account found!")
    conn.close()
    sys.exit(1)

stored_hash = result[0]

if hash_password(root_password) != stored_hash:
    print("The root-password is wrong. Stopping process!")
    conn.close()
    sys.exit(1)

print("Root access granted.")

# ---- asking if you want to list the users ----
while True:
    listing_accounts = input("Do you wanna see all accounts? (yes/no): ")

    if listing_accounts == "yes":
        cursor.execute("SELECT id, username FROM users")
        for row in cursor.fetchall():
            print(row)
        break
    elif listing_accounts == "no":
        break
    else:
        print("Invalid input!")

conn.close()

# ---- asking if u want to delete a user ----

while True:
    delete_question = input("Do you want to delete a user? (yes/no): ")

    if delete_question == "yes":
        break
    elif delete_question == "no":
        sys.exit(1)
    else:
        print("Invalid choice.")

# ---- deleating the account of choice ----

username = input("Username to delete: ")

conn = sqlite3.connect("database/accounts.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE username = ?", (username,))

conn.commit()

if cursor.rowcount == 0:
    print(f"No user with the name {username} found.")
else:
    print(f"Deleted user named '{username}'.")

conn.close()
