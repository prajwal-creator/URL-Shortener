import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("800x400")
root.title("URL Shortener")
root.configure(bg="#49A")
url_slot1 = StringVar()
url_slot2 = StringVar()

def urlshortener():
    main_url = url_slot1.get()
    shortened_url = pyshorteners.Shortener().tinyurl.short(main_url)
    url_slot2.set(shortened_url)

def copyurl():
    shortened_url = url_slot2.get()
    pyperclip.copy(shortened_url)

Label(root,height=2, width=20, text="My URL Shortener", font="poppins").pack(pady=25)
Entry(root, width=100,bd=2, textvariable=url_slot1).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=10)
Entry(root,width=75,bd=2, textvariable=url_slot2).pack(pady=10)
Button(root, text="Copy URL",command=copyurl).pack(pady=5)

root.mainloop()
