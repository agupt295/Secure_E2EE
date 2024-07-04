import boto3

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