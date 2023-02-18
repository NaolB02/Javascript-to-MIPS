from ast import parse
import tkinter as tk
from tkinter import filedialog
from tkinter.tix import IMAGETEXT

class PageOne(tk.Frame):
    def __init__(self, master, next_page_callback):
        super().__init__(master)
        self.next_page_callback = next_page_callback

        # create the canvas
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        # add the buttons to the canvas
        self.button_style = {'background': '#007bff', 'foreground': 'white', 'font': ('Arial', 14)}

        self.button1 = tk.Button(self.canvas, text="Open Editor", width=20, command=self.next_page, **self.button_style)
        self.button1.place(relx=0.3, rely=0.7, anchor='center')

        self.button2 = tk.Button(self.canvas, text="Choose File", width=20, command=self.choose_file, **self.button_style)
        self.button2.place(relx=0.7, rely=0.7, anchor='center')

        # place the background image behind the buttons
        self.bg_image = tk.PhotoImage(file="code.gif")


        self.canvas.create_image(0, 0, image=self.bg_image, anchor='nw')
        self.canvas.tag_lower(self.bg_image)

        self.canvas.create_text(400, 200, text="JS to Mips Compiler!", font=('Arial', 50), fill='white', anchor=tk.CENTER)

        # add the button windows to the canvas
        self.button1_window = self.canvas.create_window(180, 360, anchor='nw', window=self.button1)
        self.button2_window = self.canvas.create_window(420, 360, anchor='nw', window=self.button2)

    def next_page(self):
        self.next_page_callback()
    
    def choose_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)

class PageTwo(tk.Frame):
    def __init__(self, master, prev_page_callback):
        super().__init__(master, width=800, height=600)
        self.prev_page_callback = prev_page_callback

        # Create the widgets for the second page

        self.button_style = {'background': '#007bff', 'foreground': 'white', 'font': ('Arial', 14)}

        self.input_text = tk.Text(self, width=50, height=40, bg='black', fg='white')
        self.input_text.pack(side=tk.LEFT, padx=10, pady=10)


        self.compile_button = tk.Button(self, text="Compile", command=self.compile_code, **self.button_style)
        self.compile_button.pack(side=tk.BOTTOM, padx=10, pady=10)


        self.output_text = tk.Text(self, width=50, height=37)
        self.output_text.pack(side=tk.LEFT, padx=5, pady=10)



    def prev_page(self):
        self.prev_page_callback()
    
    def compile_code(self):
        # Get the input code from the text area
        code = self.input_text.get("1.0", "end-1c")

        # Parse the input code
        parsed_code = parse(code)

        # Generate the MIPS code from the parsed code
        mips_code =  "" #generate_mips(parsed_code)

        # Execute the generated MIPS code and capture the output
        result = mips_code

        # Display the output in the output text area
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        root.geometry("800x600")
        # Create the container for the pages
        self.page_container = tk.Frame(self.master)
        self.page_container.pack(fill=tk.BOTH, expand=True)

        # Create the pages and add them to the container
        self.page_one = PageOne(self.page_container, self.show_page_two)
        self.page_two = PageTwo(self.page_container, self.show_page_one)
        self.page_one.pack(fill=tk.BOTH, expand=True)
        self.page_two.pack(fill=tk.BOTH, expand=True)

        # Show the first page
        self.show_page_one()

    def show_page_one(self):
        self.page_one.pack(fill=tk.BOTH, expand=True)
        self.page_two.pack_forget()

    def show_page_two(self):
        self.page_two.pack(fill=tk.BOTH, expand=True)
        self.page_one.pack_forget()

root = tk.Tk()
app = MainApplication(master=root)
app.mainloop()
