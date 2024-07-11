def encrypt(text, shift):
    result = ""

    # traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
            
        # Encrypt digits
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        
        # Encrypt special characters
        elif char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', ',', '.', '<', '>', '/', '?']:
            result += chr((ord(char) + shift - 33) % 15 + 33)

        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (e/d): ")
        if choice.lower() not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice.lower() == 'e':
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)

        another = input("Do you want to process another message? (y/n): ")
        if another.lower() != 'y':
            break

if __name__ == "__main__":
    main()
