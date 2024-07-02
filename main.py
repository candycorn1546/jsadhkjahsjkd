import os
import subprocess

# Insecure use of subprocess with user input
def run_command(command):
    subprocess.run(command, shell=True, check=True)

def greet(name):
    # Potential vulnerability: unvalidated input
    print(f"Hello, {name}!")

def add(a, b):
    # Improper type handling
    return a + b


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet(user_name)

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(f"The sum is: {add(num1, num2)}")

    command = input("Enter a shell command to run: ")
    run_command(command)

    # Insecurely loading environment variables
    secret_key = os.getenv('SECRET_KEY')
    print(f"Your secret key is: {secret_key}")

    username = 'helloWorld'
    password = 'password'
    
    print(username,password)
