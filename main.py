import tkinter as tk
from src.operations import load, fileDecrypt

window = tk.Tk()
window.title('K9Vault')
window.geometry('600x300')
frame = tk.Frame(window)
frame.pack(pady=20)
style = {
    'button': {
        'bg': '#1B1B1B',
        'fg': '#1B1B1B',
        'font': ('Helvetica', 12, 'bold'),
        'activebackground': '#1B1B1B',
        'borderwidth': 0,
        'relief': 'flat'
    },
    'entry': {
        'show': '*',
        'width': 30,
        'bg': '#1B1B1B',
        'font': ('Helvetica', 12),
        'borderwidth': 2,
        'relief': 'groove'
    }
}

loadButton = tk.Button(frame, text='File Upload', command=load, **style['button'])
loadButton.pack(pady=10)
passwordEntry = tk.Entry(frame, **style['entry'])
passwordEntry.pack(pady=10)
decryptButton = tk.Button(frame, text='File Decrypt', command=fileDecrypt, **style['button'])
decryptButton.pack(pady=10)
userGuide = tk.Label(frame, text='Usage Guide:\n1. First, upload your photo and take the key from the console.\n2. Then enter the key and upload the encrypted photo.\n3. Your encrypted file will now be decrypted and saved in the folder.', font=('Helvetica', 10))
userGuide.pack(pady=10)
window.mainloop()