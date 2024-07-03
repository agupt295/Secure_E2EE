# this is the sender file

from cryptography.fernet import Fernet
import json

# Generate and save a key (this should be done only once)
def generate_key():
    key = Fernet.generate_key()

    # Save the key to a file named 'key.key'
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

    print("Encryption key generated and saved to key.key")

def load_key():
    return open('key.key', 'rb').read()

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def send_message(message, recipient):
    key = load_key()
    encrypted_message = encrypt_message(message, key)
    
    # In a real scenario, you would send this to a cloud service
    with open('encrypted_message.txt', 'ab') as f:
        f.write(encrypted_message + b'\n')

    print(f"Message sent to {recipient}")

if __name__ == "__main__":
    recipient = "receiver@example.com"
    generate_key()

    message = "Hello, this is a secure message."
    send_message(message, recipient)