from encryption import encrypt_message
from decryption import decrypt_message
from create_client import new_client

# KMS key ARN of the User you want to send te message to
alias_name = "User-01"
# key_arn = new_client(alias_name)
key_arn = 'arn:aws:kms:us-east-1:058264392865:key/762a603a-8d8b-47c1-a9eb-1988160b0e18'
# Encrypt a message
plaintext_message = "Hello, this is a secure message."
ciphertext = encrypt_message(plaintext_message, key_arn)
print(f"Encrypted message: {ciphertext}")

# Decrypt the message
decrypted_message = decrypt_message(ciphertext, key_arn)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")