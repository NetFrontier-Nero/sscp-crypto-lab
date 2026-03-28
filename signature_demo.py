# signature_demo.py
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def signature_demo():
    key = RSA.generate(2048)
    message = b"Verify me!"
    
    # Hash the message
    h = SHA256.new(message)
    
    # Sign
    signature = pkcs1_15.new(key).sign(h)
    print(f"Signature: {signature.hex()[:60]}...")  # abbreviated
    
    # Verify
    try:
        pkcs1_15.new(key.publickey()).verify(h, signature)
        print("Signature is valid!")
    except (ValueError, TypeError):
        print("Signature verification failed.")

if __name__ == "__main__":
    signature_demo()
