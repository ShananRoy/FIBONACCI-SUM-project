from tkinter import *

root=Tk()
root.title("acsii")

root.geometry("400x400")
root.configure(background='snow')


enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)
label = Label(root, text = "Name in Ascii : ", bg="light yellow", fg="black")

def Asciiconverter():
    input_word=enter_word.get()
    
    for letter in input_word:
        label["text"]+=str(ord(letter)) + " "
        
btn=Button(root,text="show name in ascii",command=Asciiconverter,bg='gold',fg='black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)


list=["red","green","purple","blue"]
print(list) 
import random
n=random.random()
print(n)
n1=random.randint(0, 10)
print(n1)
randomlist=random.sample(range(0,20),10)
print(randomlist)
root.mainloop()