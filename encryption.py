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