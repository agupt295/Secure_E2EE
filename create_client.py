import boto3
from user import User
    
def new_client(alias_name, password):
    # Create a KMS client
    kms_client = boto3.client('kms')

    # Create a new asymmetric KMS key
    response = kms_client.create_key(
        CustomerMasterKeySpec='RSA_2048',
        KeyUsage='ENCRYPT_DECRYPT',
        Origin='AWS_KMS',
        Description=f'User: {alias_name}'
    )

    key_arn = response['KeyMetadata']['Arn']

    alias_response = kms_client.create_alias(
        AliasName=f'alias/{alias_name}',
        TargetKeyId=key_arn
    )

    user = User(alias_name, key_arn, password)
    return user