import secrets
import string

alphabets = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabets)for i in range(int(input("Enter password length : "))))

print(password)
