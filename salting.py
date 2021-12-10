# Salting Algorithm - This Algorithm takes in text,hashes it
# then salts the hashed value printing all results in the process
# Author: Joachim Wambua

import os
import hashlib

if __name__ == '__main__':
    # Implementing a Sorting Algorithm
    salting = os.urandom(32)

    # Collect user input for text to hash
    original_text = input('Enter Text to Hash & Salt: ').encode()

    # hashing the encoded input text
    hash = hashlib.pbkdf2_hmac('sha256', original_text, salting, 10000)

    # Print original Text
    print('Original value --> ' + str(original_text))

    # encoding hashed text to hexadecimal
    hashed_text = hash.hex()
    print('Hashed value --> ' + str(hashed_text))

    # Salting the hash values
    salted_hash = hash.fromhex(hash.hex())
    print('Salted Hash value --> ' + str(salted_hash))
