def cipher_caesar(text: str, offset: int) -> str:
    new_text = ""
    for index, char in enumerate(text):
        position: int = 0
        if ord(char) > 90:
            position = ord(char) - 96
            position = (position + offset) % 26 + 96
        else:
            position = ord(char) - 64
            position = (position + offset) % 26 + 64

        new_text += chr(position)
    return new_text


text1 = input()
offset1 = input()
offset1 = int(offset1)
print(cipher_caesar(text1, offset1))
