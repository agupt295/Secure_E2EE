from encryption import encrypt_message
from decryption import decrypt_message

# Your KMS key ARN
key_arn = 'arn:aws:kms:us-east-1:058264392865:alias/kms-user-key'

# Encrypt a message
plaintext_message = "Hello, this is a secure message."
ciphertext = encrypt_message(plaintext_message, key_arn)
print(f"Encrypted message: {ciphertext}")

# Decrypt the message
decrypted_message = decrypt_message(ciphertext, key_arn)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")