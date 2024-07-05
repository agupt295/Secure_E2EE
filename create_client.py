import boto3
import bcrypt

class User:
    def __init__(self, alias_name, kms_arn, password):
        self.alias = alias_name
        self.kms_arn = kms_arn
        self.password_hash = User.hash_password(password)

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash)
    
    def get_alias_name(self):
        return self.alias
    
    def get_alias_kms_arn(self):
        return self.kms_arn
    
def new_client(alias_name, password):
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

    user = User(alias_name, key_arn, password)
    return user