# Import modules
from tkinter import *
import core.twilight as twilight

# Main
if __name__ == "__main__":

    # Commands
    def encrypt():
        text = eText.get('1.0', END)
        key  = kEntry.get()
        res  = twilight.Encrypt(text, key)
        dText.delete('1.0', END)
        dText.insert(1.0,res)

    def decrypt():
        text = dText.get('1.0', END)
        key  = kEntry.get()
        res  = twilight.Decrypt(text, key)
        eText.delete('1.0', END)
        eText.insert(1.0,res)

    # Configure windows
    root = Tk()
    root.title("Twilight | Encrypt & Decrypt text tool")
    root.resizable(0, 0)
    root.geometry("800x350")
    root.configure(background="#111111")
    
    # Items
    eText   = Text(root, height=15, width=53, fg="#d5d8dc", bg="#07000a")
    dText   = Text(root, height=15, width=53, fg="#d5d8dc", bg="#07000a")
    kEntry  = Entry(root, width=96, fg="#d5d8dc", bg="#07000a", bd=2)
    eButton = Button(root, height=2, width=44, fg="#d5d8dc", bg="#07000a", text="Encrypt text >>", command = encrypt)
    dButton = Button(root, height=2, width=44, fg="#d5d8dc", bg="#07000a", text="<< Decrypt text", command = decrypt)

    # Place
    eText.place(x=10, y=10)
    dText.place(x=410, y=10)
    kEntry.place(x=11, y=255)
    eButton.place(x=10, y=285)
    dButton.place(x=409, y=285)
    root.mainloop()