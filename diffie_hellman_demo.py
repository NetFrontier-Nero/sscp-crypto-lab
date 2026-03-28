# diffie_hellman_demo.py
import secrets

def diffie_hellman_demo():
    # Prime (p) and base (g)
    p = 23
    g = 5
    
    # Alice and Bob private keys
    a = secrets.randbelow(p)
    b = secrets.randbelow(p)
    
    # Public keys
    A = pow(g, a, p)
    B = pow(g, b, p)
    
    # Shared secret
    alice_secret = pow(B, a, p)
    bob_secret = pow(A, b, p)
    
    print(f"Alice secret: {alice_secret}")
    print(f"Bob secret: {bob_secret}")
    print(f"Shared secret matches: {alice_secret == bob_secret}")

if __name__ == "__main__":
    diffie_hellman_demo()
