import random
import string
from tkinter import *
def Algo():
    text = e1.get()
    f = list(text)
    random.shuffle(f)
    alphabet = list(string.ascii_lowercase)
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    encrypted_text = ''
    for t in f:
        if t in numbers:
            t = int(t)
        if t!=' ':
            if type(t)==str:
                if t.upper()!=t:
                    s = random.randint(1,26)
                    if alphabet.index(t)+s>=len(alphabet):
                        s-=(len(alphabet)-alphabet.index(t)-1)
                        encrypted_text+=alphabet[s]
                    else:
                        encrypted_text+=alphabet[alphabet.index(t)+s]
                else:
                    s = random.randint(1,26)
                    if alphabet.index(t.lower())+s>=len(alphabet):
                        s-=(len(alphabet)-alphabet.index(t.lower())-1)
                        encrypted_text+=alphabet[s].upper()
                    else:
                        encrypted_text+=alphabet[alphabet.index(t.lower())+s].upper()
            else:
                s = random.randint(1,10)
                if numbers.index(str(t))+s>=len(numbers):
                    s-=(len(numbers)-numbers.index(str(t))-1)
                    encrypted_text+=numbers[s]
                else:
                    encrypted_text+=numbers[numbers.index(str(t))+s]
        else:
            encrypted_text+=' '
    second_encrypted_text = ''
    for t in encrypted_text:
        if t in numbers:
            t = int(t)
        if t!=' ':
            if type(t)==str:
                if t.upper()!=t:
                    if alphabet.index(t)<=12:
                        second_encrypted_text+=alphabet[random.randint(1,12)]
                    else:
                        second_encrypted_text+=alphabet[random.randint(13,25)]
                else:
                    second_encrypted_text+=alphabet[random.randint(1,25)]
            else:
                second_encrypted_text += numbers[random.randint(0,9)]
        else:
            second_encrypted_text += numbers[random.randint(0,9)]
    l3.configure(text="Original Text: {}".format(text))
    l2.configure(text="Encrypted Text: {}".format(second_encrypted_text))
root = Tk()
root.geometry('300x300')
l1 = Label(root,text = 'Please enter in a value')
l1.pack()
e1 = Entry(root)
e1.pack()
b1 = Button(root,text ='Encrypt!',command = Algo)
b1.pack()
l3 = Label(root,text = 'Original Text: ')
l3.pack()
l2 = Label(root,text = "Encrypted Text: ")
l2.pack()
root.mainloop()