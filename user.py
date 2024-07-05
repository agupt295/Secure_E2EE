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