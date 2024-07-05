from encrypt_decrypt import encrypt_message, decrypt_message
from create_client import new_client

alias_name = "User-13-class"
alias_password = "password"
# key_arn = 'arn:aws:kms:us-east-1:058264392865:key/762a603a-8d8b-47c1-a9eb-1988160b0e18'
new_user = new_client(alias_name, alias_password)
plaintext_message = "Hello, this is a secure message."
ciphertext = encrypt_message(plaintext_message, new_user.get_alias_kms_arn())
print(f"Encrypted message: {ciphertext}")

enter_password = "password"
if new_user.check_password(enter_password):
    decrypted_message = decrypt_message(ciphertext, new_user.kms_arn)
    print(f"Decrypted message: {decrypted_message.decode('utf-8')}")

else:
    print("incorrect password")