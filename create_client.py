import boto3

def new_client(alias_name):
    # Create a KMS client
    kms_client = boto3.client('kms')

    # Create a new asymmetric KMS key
    response = kms_client.create_key(
        CustomerMasterKeySpec='RSA_2048',
        KeyUsage='ENCRYPT_DECRYPT',
        Origin='AWS_KMS',
        Description=f'New User: {alias_name}'
    )

    key_arn = response['KeyMetadata']['Arn']

    alias_response = kms_client.create_alias(
        AliasName=f'alias/{alias_name}',
        TargetKeyId=key_arn
    )

    return key_arn