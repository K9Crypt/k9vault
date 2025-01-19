from tkinter import filedialog
import asyncio
from src.encrypt import fileEncrypt
from src.decrypt import decryptFileData

def load():
    try:
        path = filedialog.askopenfilename(
            title='Select File to Encrypt',
            filetypes=[('Image Files', ('*.png', '*.jpg', '*.svg'))],
            initialdir='~'
        )
        if path:
            secret_key = "VeryLongSecretKey!@#1234567890"
            print(f'K9Crypt Encryption Key: {secret_key}')
            asyncio.run(fileEncrypt(path, secret_key))
    except Exception as error:
        print(f'K9Crypt Error: {str(error)}')

def fileDecrypt():
    try:
        enc_path = filedialog.askopenfilename(
            title='Select Encrypted File to Decrypt',
            filetypes=[('K9Crypt Files', '*.k9crypt')],
            initialdir='~'
        )
        if enc_path:
            secret_key = "VeryLongSecretKey!@#1234567890"
            asyncio.run(decryptFileData(enc_path, secret_key))
    except Exception as error:
        print(f'K9Crypt Error: {str(error)}')
