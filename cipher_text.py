import gradio as gr


def encrypt_decrypt(text, mode):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper()
    result = ""

    if mode == "Encrypt":
        for char in text:
            if char in alphabet:
                shifted_index = (alphabet.index(char) + 3) % 26
                result += alphabet[shifted_index]
            elif char == ' ':
                result += ''  # Append space character as 's'
            else:
                print('Invalid character:', char)
    elif mode == "Decrypt":
        for char in text:
            if char in alphabet:
                shifted_index = (alphabet.index(char) - 3) % 26
                result += alphabet[shifted_index]
            elif char == '':
                result += ' '  # Append space character
            else:
                print('Invalid character:', char)
    else:
        print('Invalid mode:', mode)

    return result


iface = gr.Interface(
    fn=encrypt_decrypt,
    inputs=["text", gr.inputs.Radio(["Encrypt", "Decrypt"], label="Mode")],
    outputs="text",
    title="Simple Substitution Cipher",
    description="Enter the text to encrypt or decrypt using a simple substitution cipher.",
    examples=[
        ["HELLO WORLD", "Encrypt"],
        ["KHOOR ZRUOG", "Decrypt"],
    ]
)

iface.launch(share=True)
