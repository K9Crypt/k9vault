from k9crypt import K9Crypt
import asyncio
import base64
import os

async def fileEncrypt(file_path, secret_key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            data_str = base64.b64encode(data).decode('utf-8')
            encryptor = K9Crypt(secret_key)
            encrypted = await encryptor.encrypt(data_str)
            
            with open('image.k9crypt', 'wb') as enc_file:
                enc_file.write(encrypted.encode('utf-8'))
            print('File encrypted successfully with K9Crypt signature.')
    except Exception as error:
        print('Encryption error:', str(error))
