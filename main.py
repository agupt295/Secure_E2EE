from encrypt_decrypt import encrypt_message, decrypt_message
from create_client import new_client

def send_message(user, message_to_send):
    user.message_received(message_to_send)

def read_message(user, symmetric_password):
    if user.check_password(symmetric_password):
        decrypted_message = decrypt_message(ciphertext, user.kms_arn)
        print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
    else:
        print("incorrect password")

alias_name = "User_B"
symmetric_password = "password"
new_user = new_client(alias_name, symmetric_password)
message_to_send = f'Hello user: {new_user.get_alias_name()}, there is a secure message.'
ciphertext = encrypt_message(message_to_send, new_user.get_alias_kms_arn())

send_message(new_user, ciphertext)
enter_password_to_validate = "password"
read_message(new_user, enter_password_to_validate)
read_message(new_user, "pasword")