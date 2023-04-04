#This program encrypts a message using Caesar Cipher
def caesar_cipher(message, shift):
    # Convert message to uppercase
    message = message.upper()

    # Create an empty string to store the encrypted message
    encrypted_message = ""

    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Shift the letter by the specified amount
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            # Add the shifted letter to the encrypted message
            encrypted_message += shifted_char
        else:
            # If the character is not a letter, add it to the encrypted message as is
            encrypted_message += char

    return encrypted_message


# Ask user for input
message = input("Enter a message to encrypt: ")
shift = int(input("Enter a shift amount: "))

# Encrypt the message
encrypted_message = caesar_cipher(message, shift)

# Print the encrypted message
print("Encrypted message:", encrypted_message)
