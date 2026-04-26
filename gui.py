import tkinter as tk
from compressionmodule import compress, decompress

def compression(i, o):
    compress(i,o)

window = tk.Tk()
window.title("Compression And Decompression App")
window.geometry("600x400")
window.config(bg="grey")

input_entry = tk.Entry(window)
input_label = tk.Label(window, text="File To Be Compressed")

output_entry = tk.Entry(window)
output_label = tk.Label(window, text="Name Of The Compressed File")

input_entry.grid(row=0, column=1, padx=5, pady=5)
input_label.grid(row=0, column=0)

output_label.grid(row=1, column=0)
output_entry.grid(row=1, column=1, padx=5, pady=5)

compress_button = tk.Button(window, text="Compress", command = lambda:compress(input_entry.get(), output_entry.get()))
compress_button.grid(row=2, column=1)

#output_entry.pack()

window.mainloop()