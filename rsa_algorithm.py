
# RSA Algorithm in Python
# Author: Joachim Wambua
from decimal import Decimal


# Function to obtain GCD of the two large prime numbers for RSA
def find_gcd(x, y):
    if y != 0:
        return find_gcd(y, x % y)
    else:
        return x

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('---RSA Algorithm Python---')
    prime_one = int(input('Enter 1st Large Prime Number: '))
    prime_two = int(input('Enter 2nd Large Prime Number: '))
    message = int(input('Enter message to be encrypted: '))

    # Evaluate totient & product
    product = prime_one * prime_two

    # Evaluate Totient
    totient = ((prime_one - 1) * (prime_two -1))

    for index in range(2, totient):
        if find_gcd(index, totient) == 1:
            break

    for index2 in range(1, 10):
        n = 1 + index2*totient
        if n % index == 0:
            m = int(n/index)
            break

    cipher = Decimal(0)
    cipher = pow(message, index)
    cipher_text = cipher % product

    decryption = Decimal(0)
    decryption = pow(cipher_text, m)
    decrypted_text = decryption % product

    # print('product: ', str(product))
    # print('gcd: ', str(index))
    print('totient: ', str(totient))
    print('m: ', str(m))
    print('cipher text: ', str(cipher_text))
    print('decrypted text: ', str(decrypted_text))