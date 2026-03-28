# aes_demo.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_demo():
    key = get_random_bytes(16)  # AES-128
    cipher = AES.new(key, AES.MODE_CBC)from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_demo():
    key = get_random_bytes(16)  # AES-128 key
    cipher = AES.new(key, AES.MODE_CBC)
    
    message = b"Secret SSCP Data!"
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    
    print(f"Key (hex): {key.hex()}")
    print(f"IV (hex): {cipher.iv.hex()}")
    print(f"Ciphertext: {ciphertext.hex()}")
    
    # Decrypt
    decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
    print(f"Decrypted: {decrypted.decode()}")

if __name__ == "__main__":
    aes_demo()
    
    message = b"Secret SSCP Data!"
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    
    print(f"Ciphertext: {ciphertext.hex()}")
    
    # Decrypt
    decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
    print(f"Decrypted: {decrypted.decode()}")

if __name__ == "__main__":
    aes_demo()
