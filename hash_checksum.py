# -*- coding: utf-8 -*-
"""
Compute hash of a file and dumps it into the console.
"""
import tkinter as tk
from tkinter import filedialog
import hashlib

if __name__ == "__main__":
    root = tk.Tk()
    file_path = filedialog.askopenfilename(
        title="Select a file check its hash")
    root.destroy()
    print("File:", file_path, "\nHash:")

    with open(file_path, "rb") as f:
        bytes_ = f.read()
    print("MD5: " + hashlib.md5(bytes_).hexdigest())
    print("SHA1: " + hashlib.sha1(bytes_).hexdigest())
    print("SHA256: " + hashlib.sha256(bytes_).hexdigest())
    print("SHA512: " + hashlib.sha512(bytes_).hexdigest())
    input("Press enter to continue...")
