import numpy as np
import time

# Given K matrix
K = np.array([[3, 2], [3, 5]])

# Function to convert a string to a list of numbers (a=0, b=1, ..., z=25)
def string_to_numbers(s):
    return [ord(c) - ord('a') for c in s]

# Function to convert a list of numbers to a string
def numbers_to_string(nums):
    return ''.join(chr(num + ord('A')) for num in nums)

# Hill cipher encryption function
def hill_cipher_encrypt(plaintext, K):
    plaintext = plaintext.lower()
    if len(plaintext) % 2 != 0:
        plaintext += 'x'  # Add 'x' to make the length even if it's odd

    numbers = string_to_numbers(plaintext)
    encrypted_numbers = []

    for i in range(0, len(numbers), 2):
        vector = np.array(numbers[i:i+2])
        encrypted_vector = np.dot(K, vector) % 26
        encrypted_numbers.extend(encrypted_vector)

    return numbers_to_string(encrypted_numbers)

# Get input
plaintext = input("Enter the string to encrypt: ")

# Start encryption time
start_time = time.time()

# Perform encryption
ciphertext = hill_cipher_encrypt(plaintext, K)

# End encryption time
end_time = time.time()

# Output results
print("Encrypted string:", ciphertext)
print("Time taken for encryption:", end_time - start_time, "seconds")