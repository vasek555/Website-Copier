import tkinter as tk
from tkinter import messagebox, ttk
import wget
import threading

def deep_copy_website(url, destination):
    try:
        wget.download(url, out=destination)
        messagebox.showinfo("Success", "Website copied successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_copy():
    url = url_entry.get()
    destination = dest_entry.get()
    threading.Thread(target=deep_copy_website, args=(url, destination)).start()

root = tk.Tk()
root.title("Website Copier")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

url_label = ttk.Label(mainframe, text="URL")
url_label.grid(column=1, row=1, sticky=tk.W)

url_entry = ttk.Entry(mainframe, width=20)
url_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

dest_label = ttk.Label(mainframe, text="Destination")
dest_label.grid(column=1, row=2, sticky=tk.W)

dest_entry = ttk.Entry(mainframe, width=20)
dest_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

copy_button = ttk.Button(mainframe, text="Copy", command=start_copy)
copy_button.grid(column=2, row=3, sticky=tk.E)

root.mainloop()