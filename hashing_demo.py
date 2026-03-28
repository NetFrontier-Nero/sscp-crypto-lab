# hashing_demo.py
import hashlib

def hash_demo():
    message = "Hello SSCP Crypto Lab!"
    
    # SHA-256
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    print(f"SHA-256: {sha256_hash}")
    
    # SHA-3 (SHA3-256)
    sha3_hash = hashlib.sha3_256(message.encode()).hexdigest()
    print(f"SHA3-256: {sha3_hash}")

if __name__ == "__main__":
    hash_demo()
