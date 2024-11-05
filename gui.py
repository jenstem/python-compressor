import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog


def open_file():
    """
    Opens a file dialog for the user to select a file to compress.

    Returns:
        str: The path of the selected file.
    """
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file to compress")
    return filename


def compression(i, o):
    """
    Compresses the specified input file and saves it to the output location.

    Args:
        i (str): The path of the input file to be compressed.
        o (str): The path where the compressed file will be saved.
    """
    compress(i, o)

def decompression(i, o):
    """
    Decompresses the specified input file and saves it to the output location.

    Args:
        i (str): The path of the input file to be decompressed.
        o (str): The path where the decompressed file will be saved.
    """
    decompress(i, o)


window = tk.Tk()
window.title("Compression Engine")
window.geometry("300x200")


# Entry Fields
input_entry = tk.Entry(window, width=50)
output_entry = tk.Entry(window, width=50)


# Buttons
compress_button = tk.Button(window, text="Compress", command=lambda: compression(open_file(), "CompressedOutput1.txt"))
compress_button.grid(row=2, column=1, padx=100, pady=30)

decompress_button = tk.Button(window, text="Decompress", command=lambda: decompression(open_file(), "DecompressedOutput1.txt"))
decompress_button.grid(row=3, column=1, padx=100, pady=10)


window.mainloop()
