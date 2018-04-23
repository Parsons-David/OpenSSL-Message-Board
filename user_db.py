#!/usr/bin/python3

import random, hashlib, threading

lock = threading.Lock()

# Authenticate and/or create a user
# With the given username and password
# username_password = {
#     "USERNAME" : "Bighead",
#     "PASSWORD" : "username"
# }
# Returns true if the username password combo is valid
# or if a new user has been created
def authenticate(username_and_password):
    
    username = username_and_password["USERNAME"]
    password = username_and_password["PASSWORD"]

    found = False;
    nextline = False;
    getsalt = False;
    stored_password = ""
    salt = ""
    
    lock.acquire()    

    # First, check to see if the username already exists
    with open("user_db.txt") as db:
        for line in db:
            if (line == (username + '\n')) or nextline:
                if getsalt:
                    salt = line[:-1]
                    break
                elif nextline:
                    stored_password = line[:-1]
                    getsalt = True
                else:
                    found = True
                    nextline = True
            else:
                found = False
    
    lock.release()

    # If the username doesn't already exist, salt, hash, and store the new credentials in the system, and authenticate
    if found:
        password = salt + password

        hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        if hash_pass == stored_password:
            return True
        else:
            return False
    else:
        salt_hash_store(username, password)
        return True    

def salt_hash_store(username, password):

    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Create and add the salt to the password
    chars = []
    for i in range(16):
        chars.append(random.choice(ALPHABET))
    chars = "".join(chars)

    password = chars + password

    # Hash the password
    secret_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()

    lock.acquire()

    with open("user_db.txt", 'a') as out:
        out.write(username + '\n')
        out.write(secret_pass + '\n')
        out.write(chars + '\n')

    lock.release()

# Write your testing in here
def main():
    pass

if __name__ == '__main__':
    main()
