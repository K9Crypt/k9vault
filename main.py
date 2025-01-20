from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from src.operations import load, fileDecrypt
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_github():
    webbrowser.open('https://github.com/k9crypt/k9vault')

window = Tk()
window.geometry("700x346")
window.configure(bg = "#121212")
window.title("K9Vault")

canvas = Canvas(
    window,
    bg = "#121212",
    height = 346,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    51.0,
    fill="#121212",
    outline="")

canvas.create_rectangle(
    0.0,
    315.0,
    700.0,
    346.0,
    fill="#151515",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    35.0,
    25.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=500,
    highlightthickness=0,
    command=open_github,
    relief="flat"
)
button_1.place(
    x=609.0,
    y=14.0,
    width=81.0,
    height=23.0
)

canvas.create_text(
    20.0,
    324.0,
    anchor="nw",
    text="v0.2 - BETA",
    fill="#FFFFFF",
    font=("Outfit Regular", 10 * -1)
)

canvas.create_rectangle(
    50.0,
    73.0,
    251.0,
    273.0,
    fill="#151515",
    outline="")

canvas.create_text(
    102.0,
    88.0,
    anchor="nw",
    text="Select the image",
    fill="#FFFFFF",
    font=("Outfit Regular", 13 * -1)
)

canvas.create_text(
    91.0,
    104.0,
    anchor="nw",
    text="you want to encrypt.",
    fill="#FFFFFF",
    font=("Outfit Regular", 13 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: load(),
    relief="flat"
)
button_2.place(
    x=74.0,
    y=143.0,
    width=152.0,
    height=100.0
)

canvas.create_rectangle(
    449.0,
    73.0,
    650.0,
    273.0,
    fill="#151515",
    outline="")

canvas.create_text(
    501.0,
    88.0,
    anchor="nw",
    text="Select the image",
    fill="#FFFFFF",
    font=("Outfit Regular", 13 * -1)
)

canvas.create_text(
    490.0,
    104.0,
    anchor="nw",
    text="you want to decrypt.",
    fill="#FFFFFF",
    font=("Outfit Regular", 13 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fileDecrypt(),
    relief="flat"
)
button_3.place(
    x=473.0,
    y=143.0,
    width=152.0,
    height=100.0
)
window.resizable(False, False)
window.mainloop()