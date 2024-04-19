import base64
import cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def derive_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

    
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 


# Uncomment if you have not generated the key yet        
# write_key()

def load_key(password):
    file = open("key.key", "rb")
    salt = file.read()
    file.close()
    key = derive_key_from_password(password.encode(), salt)
    return key


mstr_pwd = input("Enter your Master password: ")

# Uncomment the line below if you have not set a master password yet
# write_key()
key = load_key(mstr_pwd)
fer = Fernet(key)

def view():
    try:
        with open('password.txt', 'r') as file:
            for line in file.readlines():
                data = line.rstrip()
                account, encrypted_password = data.split("|")
                try: 
                    decrypted_password = fer.decrypt(encrypted_password.encode()).decode()
                    print("Account:", account, "| Password:", decrypted_password) 
                except cryptography.fernet.InvalidToken:
                    print("Incorrect password. Unable to decrypt for account: ", account)
    except FileNotFoundError:
        print("Password file not found. It seems there are no passwords stored yet.")

def add():
    name = input("Enter Account name: ")
    pwd = input("Enter Account password: ")
    with open("password.txt", "a") as file:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        file.write(name + "|" + encrypted_pwd + "\n")


while True:
    user = input("Do you want to view or add a password or q to quit (add/view)? ").lower()
    if user == "q":
        break

    if user == "add":
        add()
    elif user == "view":
        view()
    else:
        continue