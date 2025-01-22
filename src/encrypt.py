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

async def fileEncrypt(file_path, secret_key):
    try:
        print("\n=== File Information ===")
        print(f"File name: {os.path.basename(file_path)}")
        print(f"Full path: {os.path.abspath(file_path)}")
        
        file_stats = os.stat(file_path)
        file_size = file_stats.st_size
        created_time = datetime.fromtimestamp(file_stats.st_ctime)
        
        print(f"Size: {format_size(file_size)}")
        print(f"Created: {created_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 22 + "\n")
        
        with open(file_path, 'rb') as file:
            print('Reading file contents...')
            data = file.read()
            data_str = base64.b64encode(data).decode('utf-8')
            encryptor = K9Crypt(secret_key)
            encrypted = await encryptor.encrypt(data_str)
            
            print('Writing encrypted data...')
            with open('image.k9crypt', 'wb') as enc_file:
                enc_file.write(encrypted.encode('utf-8'))
            print(f'\nEncryption completed successfully')
            print(f'Output file: image.k9crypt')
            print("=" * 22)
    except Exception as error:
        print('\nError during encryption:')
        print(f"► {str(error)}")
