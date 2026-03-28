# rsa_demo.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_demo():
    key = RSA.generate(2048)
    public_key = key.publickey()
    
    message = b"SSCP RSA Test"
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message)
    
    print(f"Ciphertext: {ciphertext.hex()[:60]}...")  # abbreviated
    
    # Decrypt
    decrypt_cipher = PKCS1_OAEP.new(key)
    decrypted = decrypt_cipher.decrypt(ciphertext)
    print(f"Decrypted: {decrypted.decode()}")

if __name__ == "__main__":
    rsa_demo()
