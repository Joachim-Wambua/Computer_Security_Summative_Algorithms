# Hashing Algorithm using SHA256 algorithm
# Author Joachim Wambua

# Import hashing Library
import hashlib


# Hashing Algorithm (SHA 256)
def hash256(data):
    # hashing the encoded data using SHA256
    hashed_data = hashlib.sha256(data.encode())
    # Encoding the hashed data as a hexadecimal value
    final_result = hashed_data.hexdigest()
    return final_result


# Hashing Algorithm (SHA 512)
def hash512(data):
    # hashing the encoded data using SHA512
    hashed_data = hashlib.sha512(data.encode())
    # Encoding the hashed data as a hexadecimal value
    final_result = hashed_data.hexdigest()
    return final_result


# Main Logic
if __name__ == "__main__":
    print("-----HASHING ALGORITHM----")
    print()
    # Collect value to hash
    user_data = input('Enter Message to Hash\n')
    # Get user choice for available hashing options
    user_choice = int(input('Which Hashing Algorithm would you like to use?\nEnter 1 --> SHA256\nEnter 2 --> SHA512\n'))

    # Check which hashing algorithm the user selected.
    # If SHA256
    if user_choice == 1:
        hashed = hash256(user_data)
        print('SHA256 = ' + str(hashed))
    # If SHA512
    elif user_choice == 2:
        data_hashed = hash512(user_data)
        print('SHA512 = ' + str(data_hashed))
