from tkinter import *

root = Tk()

root.configure(bg="#74cfbf")
titlebar = root.title("Author: Annonymuos")
title = Label(root, text="Vigenere Cypher Decryption and Encryption", fg="white", bg="#272e46")

title.grid(row=0, column=0, columnspan=5, pady=10, padx=30)

chars = "abcdefghijklmnopqrstuvwxyz 0123456789"
values = {chars[i]: i for i in range(len(chars))}

plainText = Entry(root, width=40)
plainText.grid(row=2, column=0, columnspan=4, ipady=15, pady=10, padx=30)
plainText.insert(0, "Enter plain text")

keyText = Entry(root, width=30)
keyText.grid(row=3, column=0, columnspan=4, pady=10, padx=30)
keyText.insert(0, "Enter key")

cipherText = Entry(root, width=40)
cipherText.grid(row=4, column=0, columnspan=4, ipady=15, pady=10, padx=30)
cipherText.insert(1, "Cipher output")

def process_key(msg, key):
    if len(key) >= len(msg):
        k = key[:len(msg)]
    else:
        mul, rem = divmod(len(msg), len(key))
        k = key * mul + key[:rem]
    return k

def encrypt():
    key_phrase = plainText.get().lower()
    plain_text = keyText.get()
    key = process_key(plain_text, key_phrase)
    plain = plain_text.lower()
    cipher = ''
    for i in range(len(plain)):
        c_num = (values.get(plain[i]) + values.get(key[i])) % 37
        for k, v in values.items():
            if v == c_num:
                cipher = cipher + k
    cipher.upper()
    cipherText.delete(0, END)
    cipherText.insert(0, cipher)

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

def exit():
    root.destroy()  

def clear():
    plainText.delete(0, END)
    keyText.delete(0, END)
    cipherText.delete(0, END)

encryptButton = Button(root, text="Encrypt", command=encrypt, fg='black', bg="#90EE90")
encryptButton.grid(row=1, column=1, columnspan=1, pady=10, padx=30)

decryptButton = Button(root, text="Decrypt", command=decrypt, fg='black', bg="#90EE90")
decryptButton.grid(row=1, column=2, columnspan=1, pady=10, padx=30)

resetButton = Button(root, text="Clear", command=clear, fg='black', bg="#90EE90")
resetButton.grid(row=5, column=1, columnspan=2, pady=5, padx=30)

exit = Button(root, text="Exit", command=exit, fg='black', bg="#FF0000")
exit.grid(row=6, column=1, columnspan=2, pady=10, padx=30)

root.mainloop()
