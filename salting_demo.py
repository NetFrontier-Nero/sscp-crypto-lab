# salting_demo.py
import hashlib
import os

def generate_salt():
    # 16-byte cryptographic salt
    return os.urandom(16)

def hash_with_salt(password: str, salt: bytes):
    # Combine password + salt
    salted_input = salt + password.encode()

    # SHA-256 hash of salted input
    hash_value = hashlib.sha256(salted_input).hexdigest()

    return hash_value

def demo():
    password = "SuperSecurePassword123"

    # Step 1: generate salt
    salt = generate_salt()

    # Step 2: hash with salt
    hashed_password = hash_with_salt(password, salt)

    print("Password:", password)
    print("Salt (hex):", salt.hex())
    print("Salted Hash (SHA-256):", hashed_password)

    print("\n--- Verification Demo ---")

    # Simulate login attempt
    attempt = "SuperSecurePassword123"
    attempt_hash = hash_with_salt(attempt, salt)

    if attempt_hash == hashed_password:
        print("Authentication SUCCESS (hashes match)")
    else:
        print("Authentication FAILED")

if __name__ == "__main__":
    demo()
