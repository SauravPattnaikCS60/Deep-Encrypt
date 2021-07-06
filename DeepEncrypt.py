from tkinter import *
from project import *
from encrypt import *
import ast


def command_encode():
    if path.get() is None:
        return
    path1 = str(path.get().replace("\\", "\\\\"))
    file = open(path1)
    text = file.read()
    file.close()
    if pin_entry.get() is None or plug_entry.get() is None or pos_entry.get() is None:
        return
    enigma = EnigmaEncrypt(int(pin_entry.get()), str(plug_entry.get()))
    enigma.setRotorPosition(str(pos_entry.get()))
    enigma_text = ""
    for word in text.split():
        enigma_text = enigma_text + enigma.process(word) + " "

    hf = HuffmanCoding()
    val = hf.compress(enigma_text)
    reverse_list = hf.return_reverse()
    file = open("encrypted.txt", 'w')
    file.write(val)
    file.close()
    file = open("reverse.txt", 'w')
    file.write(str(reverse_list))
    file.close()
    lb.delete(0, END)
    lb.insert(END, val)


def command_decode():
    if path_entry.get() is None:
        return
    path1 = str(path.get().replace("\\", "\\\\"))
    file = open(path1)
    text = file.read().replace(' ', '')
    file.close()
    file = open('reverse.txt')
    reverse = ast.literal_eval(file.read())
    file.close()
    hf = HuffmanCoding()
    hf_text = hf.decode(text, reverse)
    if pin_entry.get() is None or plug_entry.get() is None or pos_entry.get() is None:
        return
    enigma = EnigmaEncrypt(int(pin_entry.get()), str(plug_entry.get()))
    enigma.setRotorPosition(str(pos_entry.get()))
    #enigma_text = enigma.process(hf_text)
    enigma_text = ""
    for word in hf_text.split():
        enigma_text = enigma_text+enigma.process(word)+" "
    file = open("decoded.txt", 'w')
    file.write(enigma_text)
    file.close()
    lb.delete(0,END)
    lb.insert(END,enigma_text)

window = Tk()

l1 = Label(window, text="Specify the file path")
l1.grid(row=0, column=0)

path = StringVar()

path_entry = Entry(window, textvariable=path)
path_entry.grid(row=0, column=2, columnspan=4)

l2 = Label(window, text="Pin")
l2.grid(row=0, column=5)
pin = IntVar()
pin_entry = Entry(window, textvariable=pin)
pin_entry.grid(row=0, column=6)

l3 = Label(window, text="Plug")
l3.grid(row=1, column=5)
plug = StringVar()
plug_entry = Entry(window, textvariable=plug)
plug_entry.grid(row=1, column=6)

l4 = Label(window, text="Pos")
l4.grid(row=2, column=5)
pos = StringVar()
pos_entry = Entry(window, textvariable=pos)
pos_entry.grid(row=2, column=6)


encode = Button(window, text="Encode", command=command_encode)
encode.grid(row=1, column=0)

decode = Button(window, text="Decode", command=command_decode)
decode.grid(row=1, column=1)

lb = Listbox(window, height=15, width=45)
lb.grid(row=3, column=0, columnspan=4)

window.mainloop()
