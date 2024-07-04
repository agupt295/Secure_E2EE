import boto3

def encrypt_message(plaintext, key_id):
    # Create a KMS client
    kms_client = boto3.client('kms', region_name='us-east-1')

    # Encrypt the plaintext
    response = kms_client.encrypt(
        KeyId=key_id,
        Plaintext=plaintext,
        EncryptionAlgorithm='RSAES_OAEP_SHA_1'
    )

    # Get the encrypted data
    ciphertext = response['CiphertextBlob']
    return ciphertext

def decrypt_message(ciphertext, key_arn):
    # Create a KMS client
    kms_client = boto3.client('kms', region_name='us-east-1')

    # Decrypt the ciphertext
    response = kms_client.decrypt(
        # CiphertextBlob=ciphertext
        KeyId=key_arn,
        CiphertextBlob=ciphertext,
        EncryptionAlgorithm='RSAES_OAEP_SHA_1'
    )

    # Get the plaintext
    plaintext = response['Plaintext']
    return plaintext

# Your KMS key ARN
# key_arn = 'arn:aws:kms:us-east-1:058264392865:key/a013113a-0f7d-4a02-a7f4-0d973814dbca'
key_arn = 'arn:aws:kms:us-east-1:058264392865:alias/kms-user-key'

# Encrypt a message
plaintext_message = "Hello, this is a secure message."
ciphertext = encrypt_message(plaintext_message, key_arn)
print(f"Encrypted message: {ciphertext}")

# Decrypt the message
decrypted_message = decrypt_message(ciphertext, key_arn)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")