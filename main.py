import os

# Hard-coded secret
api_key = "12345-ABCDE"

# Command injection vulnerability
def delete_file(filename):
    os.system(f"rm {filename}")

# SQL injection vulnerability
def get_user_info(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

# Insufficient input validation
def is_valid_age(age):
    return int(age) > 18

# Example usage
if __name__ == "__main__":
    print(delete_file("test.txt"))
    print(get_user_info("1 OR 1=1"))
    print(is_valid_age("20"))
