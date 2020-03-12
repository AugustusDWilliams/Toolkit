from cryptography.fernet import Fernet



def encrypt(msg, key):
    f = Fernet(key)
    encrypted_msg = f.encrypt(msg.encode())
    return encrypted_msg

def decrypt(msg, key):
    f = Fernet(key)
    decrypted_msg = f.decrypt(msg).decode()
    return decrypted_msg

if __name__ == "__main__":
    key = Fernet.generate_key()
    msg = 'sample message'
    e_msg = encrypt(msg, key)
    print(e_msg)
    print(decrypt(e_msg, key))


