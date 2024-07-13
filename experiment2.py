import numpy as np
import time
from itertools import product

# Plaintext and ciphertext
plaintext = "helpme"
ciphertext = "dplese"

# Mapping characters to numbers and vice versa
letter_to_index = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))
index_to_letter = dict(zip(range(26), "abcdefghijklmnopqrstuvwxyz"))

# Function to convert a string to a list of numbers
def string_to_numbers(s):
    return [letter_to_index[char] for char in s.lower()]

# Function to convert a list of numbers to a string
def numbers_to_string(nums):
    return ''.join(index_to_letter[num % 26] for num in nums)

# Function to decrypt using Hill cipher
def hill_cipher_decrypt(ciphertext, K_inv):
    ciphertext_numbers = string_to_numbers(ciphertext)
    decrypted_numbers = []

    for i in range(0, len(ciphertext_numbers), 2):
        vector = np.array(ciphertext_numbers[i:i+2])
        decrypted_vector = np.dot(K_inv, vector) % 26
        decrypted_numbers.extend(decrypted_vector)

    return numbers_to_string(decrypted_numbers)

# Function to compute the modular inverse of a given matrix modulo 26
def mod_inverse_matrix(K):
    det = int(np.round(np.linalg.det(K)))  # Compute the determinant
    det_inv = pow(det, -1, 26)  # Compute the modular inverse of the determinant modulo 26
    K_adj = np.array([[K[1,1], -K[0,1]], [-K[1,0], K[0,0]]])  # Compute the adjugate matrix
    K_inv = (det_inv * K_adj) % 26  # Compute the inverse matrix
    return K_inv

# Start brute force attack
start_time = time.time()
found = False

# Try all possible matrices
for matrix in product(range(26), repeat=4):
    K = np.array(matrix).reshape(2, 2)
    print(f"Trying key matrix: \n{K}")  # Print each attempted key matrix
    if np.round(np.linalg.det(K)) % 26 == 0:
        continue  # Skip if the determinant is 0 (no inverse exists)

    try:
        K_inv = mod_inverse_matrix(K)
        decrypted_text = hill_cipher_decrypt(ciphertext, K_inv)
        if decrypted_text == plaintext:
            print(f"Key matrix found: \n{K}")
            print(f"Decrypted text: {decrypted_text}")
            found = True
            break
    except ValueError:
        continue  # Skip if inverse matrix calculation fails

end_time = time.time()

if not found:
    print("No valid key matrix found.")
print("Time taken for brute force attack:", end_time - start_time, "seconds")
