import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file to compress")
    return filename


def compression(i, o):
    compress(i, o)

def decompression(i, o):
    decompress(i, o)


window = tk.Tk()
window.title("Compression Engine")
window.geometry("300x200")


# Entry Fields
input_entry = tk.Entry(window, width=50)
output_entry = tk.Entry(window, width=50)


# Buttons
compress_button = tk.Button(window, text="Compress", command=lambda: compression(open_file(), "compressedoutput2.txt"))
compress_button.grid(row=2, column=1, padx=100, pady=30)

decompress_button = tk.Button(window, text="Decompress", command=lambda: decompression(open_file(), "decompressedoutput2.txt"))
decompress_button.grid(row=3, column=1, padx=100, pady=10)


window.mainloop()