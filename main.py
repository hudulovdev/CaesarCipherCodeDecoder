def caesar_cipher_decrypt(ciphertext):
    decrypted_text = ""
    for shift in range(26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    ascii_offset = ord('A')
                else:
                    ascii_offset = ord('a')
                
                shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                decrypted += shifted_char
            else:
                decrypted += char

        decrypted_text += f"Shift {shift}: {decrypted}\n"

    return decrypted_text

# Example usage
ciphertext = "Khoor, Zruog!"
decryption_result = caesar_cipher_decrypt(ciphertext)
print("Decryption Result:\n", decryption_result)
