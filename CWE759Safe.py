import hashlib
import os

def main():
    
    password = input("Enter password to hash: ")
    salt = os.urandom(16)
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    
    print(f"Salt: {salt}")
    print(f"Salted hashed password: {hashed_password}")
    
if __name__ == "__main__":
    main()