import tkinter as tk
from tkinter import *
from tkinter import ttk
from typing import Type
from time import sleep

root = Tk()
root.title('Vigenere Cipher')


my_notebook = ttk.Notebook(root)
my_notebook.pack()


first_frame = Frame(my_notebook, width=400, height=400)
second_frame = Frame(my_notebook, width=400, height=400)

first_frame.pack(fill="both")
second_frame.pack(fill="both", expand=1)
my_notebook.add(first_frame, text="Encryption")
my_notebook.add(second_frame, text="Decryption")

Msg = StringVar()
Encrypt_key = StringVar()


def Exit():
    root.destroy()


def Reset():
    Msg.set("")
    Encrypt_key.set("")
    cipher_text_label["text"] = ""


chars = "abcdefghijklmnopqrstuvwxyz 0123456789"
values = {chars[i]: i for i in range(len(chars))}


def process_key(msg, key):
    if len(key) >= len(msg):
        k = key[:len(msg)]
    else:
        mul, rem = divmod(len(msg), len(key))
        k = key * mul + key[:rem]
    return k


def encrypt():
    key_phrase = Encrypt_key.get().lower()
    plain_text = Msg.get()
    key = process_key(plain_text, key_phrase)
    plain = plain_text.lower()
    c = ''
    for i in range(len(plain)):
        c_num = (values.get(plain[i]) + values.get(key[i])) % 37
        for k, v in values.items():
            if v == c_num:
                c = c + k
    c.upper()
    cipher_text_label['text'] = c.upper()
    # root.update_idletasks()


def decrypt(cipher, key_phrase):
    key = process_key(cipher, key_phrase)
    cipher_text = cipher.lower()
    p = ''
    for i in range(len(cipher_text)):
        p_num = (values.get(cipher_text[i]) - values.get(key[i])) % 37
        for k, v in values.items():
            if v == p_num:
                p = p + k
    return p


# Begininning of encryption code
# the plain text handler
plain_text_label = Label(first_frame, text="Enter your plain text", font=(
    'Montserrat', 9, 'bold')).pack(pady=10),
plain_text_input = Entry(first_frame, width=50, bd="0", textvariable=Msg).pack(
    pady=10)

# encryption key handler
encryption_key_label = Label(
    first_frame, text="Enter your encryption key", font=('Montserrat', 9, 'bold')).pack(padx=0),
encryption_key_input = Entry(first_frame,  width=50,  bd="0",  textvariable=Encrypt_key).pack(
    pady=10)

# cipher text output
cipher_text_label = Label(first_frame, text="The cipher text is", font=(
    'Montserrat', 9, 'bold')).pack(pady=10)
cipher_text_label = Label(first_frame, text="", font=(
    'Montserrat', 9, 'bold'))
cipher_text_label.pack(pady=10)
# submit button
encrypt_button = Button(first_frame, text="Encrypt",
                        width="30", bd="0", command=encrypt, font=('Montserrat', 9, 'bold')).pack(pady=10)

# reset button
reset_button = Button(first_frame, text="Reset",
                      width="30", bd="0", command=Reset, font=('Montserrat', 9, 'bold')).pack(pady=10)

# exit button
exit_button = Button(first_frame, text="Exit",
                     width="30", bd="0", command=Exit, font=('Montserrat', 9, 'bold')).pack(pady=10)

# End of the encryption Code


# Beginning of the decryption section

# the cipher text handler
plain_text_label = Label(first_frame, text="Enter your plain text", font=(
    'Montserrat', 9, 'bold')).pack(pady=10),
plain_text_input = Entry(first_frame, width=50, bd="0", textvariable=Msg).pack(
    pady=10)

# encryption key handler
encryption_key_label = Label(
    first_frame, text="Enter your encryption key", font=('Montserrat', 9, 'bold')).pack(padx=0),
encryption_key_input = Entry(first_frame,  width=50,  bd="0",  textvariable=Encrypt_key).pack(
    pady=10)

# cipher text output
cipher_text_label = Label(first_frame, text="The cipher text is", font=(
    'Montserrat', 9, 'bold')).pack(pady=10)
cipher_text_label = Label(first_frame, text="", font=(
    'Montserrat', 9, 'bold'))
cipher_text_label.pack(pady=10)
# submit button
encrypt_button = Button(first_frame, text="Encrypt",
                        width="30", bd="0", command=encrypt, font=('Montserrat', 9, 'bold')).pack(pady=10)

# reset button
reset_button = Button(first_frame, text="Reset",
                      width="30", bd="0", command=Reset, font=('Montserrat', 9, 'bold')).pack(pady=10)

# exit button
exit_button = Button(first_frame, text="Exit",
                     width="30", bd="0", command=Exit, font=('Montserrat', 9, 'bold')).pack(pady=10)


root.mainloop()
