import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("CompSimple")
root.geometry("800x600")



def choose_file():
    file_path = filedialog.askopenfilename()
    print(file_path)

bgimg= tk.PhotoImage(file = "code.gif")
# tk.Label(root, text = "simple Compiler that converts \n Vanilla.js to assembly!", fg='red', i = bgimg, compound='center').pack()
tk.Label(root,text="Js to MIPS \n Compiler \n ", fg="white", i = bgimg, font=('Arial', 38), compound='center').pack()





# Define a custom style for the buttons
button_style = {'background': '#007bff', 'foreground': 'white', 'font': ('Arial', 14)}


# Create the "Button 1" widget
button1 = tk.Button(root, text="Open Editor", width=20, command=lambda: print("Button 1 clicked"), **button_style)
button1.place(relx=0.3, rely=0.7, anchor='center')


# Create the "Button 2" widget
button2 = tk.Button(root, text="Choose File", width=20, command=choose_file, **button_style)
button2.place(relx=0.7, rely=0.7, anchor='center')



root.mainloop()
