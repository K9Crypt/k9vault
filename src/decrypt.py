from k9crypt import K9Crypt
import asyncio
import base64

async def decryptFileData(enc_file_path, secret_key):
    try:
        with open(enc_file_path, 'rb') as file:
            encrypted_data = file.read().decode('utf-8')
            decryptor = K9Crypt(secret_key)
            decrypted = await decryptor.decrypt(encrypted_data)
            file_data = base64.b64decode(decrypted)
            
            with open('image.png', 'wb') as dec_file:
                dec_file.write(file_data)
            print('File decrypted successfully.')
    except Exception as error:
        print('Decryption error:', str(error))
