def caesar_cipher(text, shift):
    encrypted_text = []
    
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift % 26
            if char.islower():
                # Calculate shifted character in lowercase
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                # Calculate shifted character in uppercase
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text.append(shifted_char)
        else:
            # Keep non-alphabet characters unchanged
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

# Get input from the user
sentence = input("python is fun ")

# Encrypt the sentence using a right shift of 5
encrypted_sentence = caesar_cipher(sentence, 5)

# Print the encrypted sentence
print("udymts nx kzs!:", encrypted_sentence)


