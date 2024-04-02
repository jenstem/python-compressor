import tkinter as tk
from compressmodule import compress, decompress


def compression(i, o):
    compress(i, o)


window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")


# Entry Fields
input_entry = tk.Entry(window, width=50)
output_entry = tk.Entry(window, width=50)


# Labels
input_label = tk.Label(window, text="File to compress")
output_label = tk.Label(window, text="Compressed file")


# Buttons
compress_button = tk.Button(window, text="Compress")


# Grid Layout
input_label.grid(row=0, column=0)
output_label.grid(row=1, column=0)

input_entry.grid(row=0, column=1)
output_entry.grid(row=1, column=1)

compress_button.grid(row=2, column=1)


window.mainloop()