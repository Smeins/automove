import tkinter as tk
from tkinter import *
from tkinter import ttk 
import pyautogui
import keyboard

print("starting")

root = tk.Tk()
root.title("Automove")

label_hello = tk.Label(root, text="Welcome to Automove!")
label_hello.pack()

label_info = tk.Label(root, text="This programm will move your mouse for about 30 min!")
label_info.pack()

label_break = tk.Label(root, text="To end the programm you need to hold X for a few seconds!")
label_break.pack()

def Automove(i = 0):
    while i != 1000:
        i = i + 1
        pyautogui.moveTo(1000, 500, 1)
        pyautogui.moveTo(1500, 400, 1)
        print(i)
        try:
            if keyboard.is_pressed('x'):
             print("Programm is stopping")
             break
            else:
               pass
        except:
           pass
      

button_start = tk.Button(root, text="Starten", command=Automove)
button_start.pack(pady=10)

label_disclaimer = tk.Label(root, text="Use at your own risk!")
label_disclaimer.pack()
label_dv = tk.Label(root, text="DV for the win!")
label_dv.pack()

root.mainloop()

