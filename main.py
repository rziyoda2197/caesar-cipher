def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift * mode) % 26 + ascii_offset)
        else:
            result += char
    return result

def encode(text, shift):
    return caesar_cipher(text, shift, 1)

def decode(text, shift):
    return caesar_cipher(text, shift, -1)

text = "Hello, World!"
shift = 3

encoded_text = encode(text, shift)
decoded_text = decode(encoded_text, shift)

print(f"Matn: {text}")
print(f"Shift: {shift}")
print(f"Kodlangan matn: {encoded_text}")
print(f"Kodlangan matnni ochirgan matn: {decoded_text}")
