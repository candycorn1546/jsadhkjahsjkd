import os

# Example of a hard-coded secret
SECRET_KEY = "my_secret_key_123"

# Example of SQL injection vulnerability
def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

# Example of command injection vulnerability
def delete_file(file_name):
    os.system(f"rm {file_name}")

# Example of insufficient input validation
def is_adult(age):
    return age >= 18

# Example of an insecure deserialization vulnerability
import pickle
def deserialize_data(data):
    return pickle.loads(data)

# Example of a Cross-Site Scripting (XSS) vulnerability
def display_user_input(user_input):
    return f"<html><body>{user_input}</body></html>"

if __name__ == "__main__":
    user_input = input("Enter user input: ")
    print(display_user_input(user_input))
