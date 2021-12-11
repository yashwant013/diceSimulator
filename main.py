import random
import tkinter

root = tkinter.Tk()
root.geometry('600x600')
root.title('GUI Dice Simulator')


#label to print result
label = tkinter.Label(root, text='', font=('Helvetica',260))

#label to introduce
label2 = tkinter.Label(root, text='Welcome to Yashwant Project on Dice roll. Click to roll dice', font=('Helvetica',10))
label2.place(x=150,y=400)

def roll_dice():
    value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result=random.choice(value)
    label.configure(text=result)
    label.pack()

button = tkinter.Button(root, text='roll dice', foreground='red', command=roll_dice)
button.pack()
root.mainloop()