from k9crypt import K9Crypt
import asyncio
import base64
import os
from datetime import datetime

def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

async def decryptFileData(enc_file_path, secret_key):
    try:
        print("\n=== File Information ===")
        print(f"File name: {os.path.basename(enc_file_path)}")
        print(f"Full path: {os.path.abspath(enc_file_path)}")
        
        file_stats = os.stat(enc_file_path)
        file_size = file_stats.st_size
        created_time = datetime.fromtimestamp(file_stats.st_ctime)
        
        print(f"Size: {format_size(file_size)}")
        print(f"Created: {created_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 22 + "\n")

        with open(enc_file_path, 'rb') as file:
            print('Reading encrypted file...')
            encrypted_data = file.read().decode('utf-8')
            decryptor = K9Crypt(secret_key)
            decrypted = await decryptor.decrypt(encrypted_data)
            file_data = base64.b64decode(decrypted)
            
            print('Writing decrypted data...')
            with open('image.png', 'wb') as dec_file:
                dec_file.write(file_data)
            print(f'\nDecryption completed successfully')
            print(f'Output file: image.png')
            print("=" * 22)
    except Exception as error:
        print('\nError during decryption:')
        print(f"► {str(error)}")
