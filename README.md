# secure_messages
This project is based on more secure implementation of E2EE messaging.

### Asymmetric Key Encryption

Asymmetric encryption involves two keys: a public key and a private key. The public key is used to encrypt data, and the private key is used to decrypt data. This method ensures that even if the encrypted data is intercepted, it cannot be decrypted without the private key.

1. **Public Key**: This key is shared publicly and can be used by anyone to encrypt data.
2. **Private Key**: This key is kept secret and is used to decrypt data encrypted with the corresponding public key.

### How It Works in the Code

- **Encryption**: The `encrypt_message` function takes plaintext data and a `key_id` (which is the ID of the public key in AWS KMS). It uses the `boto3` KMS client to encrypt the data with the specified key and returns the encrypted data (ciphertext).
- **Decryption**: The `decrypt_message` function takes the encrypted data (ciphertext) and a `key_arn` (which is the ARN of the private key in AWS KMS). It uses the `boto3` KMS client to decrypt the data with the specified key and returns the original plaintext.

### An Added Layer of Security

In this implementation, an additional layer of security is added by introducing password protection. Before a message can be decrypted with the user's private key, the receiver must enter a password. This ensures that even if the private key is compromised, the message cannot be decrypted without the correct password.

To implement this functionality, the `bcrypt` was used.
