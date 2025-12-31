import string
import numpy as np


ALPHABET = string.ascii_uppercase

def letter_to_number(letter): # A=0
    letter = letter.upper()
    return ALPHABET.index(letter)

def number_to_letter(number):
    return ALPHABET[number % 26]

def text_to_numbers(text):
    return [letter_to_number(c) for c in text if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join(number_to_letter(n) for n in numbers)

def caesar_encrypt(text, shift):
    nums = text_to_numbers(text)
    shifted = [(n + shift) % 26 for n in nums]
    return numbers_to_text(shifted)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(plaintext, key):
    p = text_to_numbers(plaintext)
    k = text_to_numbers(key)
    c = [(p[i] + k[i % len(k)]) % 26 for i in range(len(p))]
    return numbers_to_text(c)

def vigenere_decrypt(ciphertext, key):
    c = text_to_numbers(ciphertext)
    k = text_to_numbers(key)
    p = [(c[i] - k[i % len(k)]) % 26 for i in range(len(c))]
    return numbers_to_text(p)

def print_grid(grid, width=5):
    for row in grid:
        print("".join(f"{cell:>{width}}" for cell in row))

def number_grid_to_text(grid):
    return np.array([[number_to_letter(num) for num in row] for row in grid])

def text_grid_to_string(textgrid):
    return ''.join(''.join(row) for row in textgrid)

def add_number_starting_at_index(grid, start_index, number):
    shape = grid.shape
    grid = grid.reshape(-1)
    for i in range(len(grid)):
        if i >= start_index:
            grid[i] += number
    return grid.reshape(shape)

def add_alternating_numbers_starting_at_index(grid, start_index, number1, number2):
    shape = grid.shape
    grid = grid.reshape(-1)
    for i in range(len(grid)):
        if i >= start_index:
            if (i - start_index) % 2 == 0:
                grid[i] += number1
            else:
                grid[i] += number2
    return grid.reshape(shape)