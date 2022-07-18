
# Cryptodome library
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

# Python Gui Library
from tkinter import *


# AES encryption function
def encrypt(message, key):
    key = key.encode()
    message = message.encode()
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(pad(message,AES.block_size)))

# AES decryption function
def decrypt (encryptedData, key):
    key = key.encode()
    raw = b64decode(encryptedData.encode())
    cipher = AES.new(key, AES.MODE_CBC, raw[:AES.block_size])
    return unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)
    


# Window
root = Tk()
# Window Name
root.title("AES Encryption/Decryption")
# Configures main window
root.configure(bg="white")
root.resizable(False, False)
root.geometry("550x260")

# Function for the encryption click event
def encryptionClick():
    clearText = encryptionInputBox.get("1.0",END)
    key = keyInputBox.get()

    # Display error messsage if keylength is below or above 16 characters
    if(not len(key)==16):
        keyInfoText.set("Error!\nPlease enter a 16 character long key!")
        keyInfoLabel.config(fg='red')
        return None
    elif(len(clearText) == 1):
        keyInfoText.set("Error!\nPlease input a value into the plain text box!")
        keyInfoLabel.config(fg='red')

    # Display error if keylength is below or above 16 characters
    else:
        keyInfoText.set("The text has been successfully encrypted.")
        keyInfoLabel.config(fg='green')
        encryptedText = encrypt(clearText, key)
        decryptionInputBox.delete("1.0",END)
        decryptionInputBox.insert(0.0, encryptedText)


# Function for the decryption click event
def decryptionClick():
    encryptedText = decryptionInputBox.get("1.0",END)
    key = keyInputBox.get()
    
    # Display error if keylength is below or above 16 characters
    if(not len(key)==16):
        keyInfoText.set("Error!\nPlease enter a 16 character long key!")
        keyInfoLabel.config(fg='red')
        return None
    elif(len(encryptedText) == 1):
        keyInfoText.set("Error!\nPlease input a value into the encryption box!")
        keyInfoLabel.config(fg='red')

    # Display error if keylength is below or above 16 characters
    else:
        keyInfoText.set("The text has been successfully decrypted.")
        keyInfoLabel.config(fg='green')
        decryptedText = decrypt(encryptedText, key)
        encryptionInputBox.delete("1.0",END)
        encryptionInputBox.insert(0.0, decryptedText)

# Text Labels
encryptionLabel = Label(font='Helvetica 11', bg="white", text="Plain Text")
decryptionLabel = Label(font='Helvetica 11', bg="white", text="Encrypted")
keyLabel = Label(font='Helvetica 11', bg="white", text="Key")
keyInfoText = StringVar()
keyInfoText.set("Please enter a 16 character key.")
keyInfoLabel = Label(font='Helvetica 9', bg="white", textvariable=keyInfoText)
# Input boxes
encryptionInputBox = Text(bg="white", width=30, height=7)
decryptionInputBox = Text(bg="white", width = 30, height=7)
keyInputBox = Entry(bg="white",width=60)
# Buttons
encryptButton = Button(text = "Encrypt", font='Helvetica 11 bold', bg="lightblue", fg="white", padx=2, pady=6, height=1, width=15, border=0, command=encryptionClick)
decryptButton = Button(text = "Decrypt", font='Helvetica 11 bold', bg="lightblue", fg="white", padx=2, pady=6, height=1, width=15, border=0, command=decryptionClick)

# Grid locations for encryption items
encryptionLabel.grid(row=1,column=0, padx=0, pady=0)
encryptionInputBox.grid(row=2, column=0, padx=10, pady=0)
encryptButton.grid(row=3, column=0)
# Grid locations for decryption items
decryptionLabel.grid(row=1,column=1)
decryptionInputBox.grid(row=2,column=1, padx=10, pady=0)
decryptButton.grid(row=3,column=1)
# Grid locations for key items
keyLabel.grid(row=4, column=0, columnspan=2)
keyInputBox.grid(row=5,column=0,columnspan=2)
keyInfoLabel.grid(row=6, column=0, columnspan=2)



root.mainloop()
