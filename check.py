from ast import parse
import tkinter as tk
from tkinter import filedialog
from tkinter.tix import IMAGETEXT

class PageOne(tk.Frame):
    def __init__(self, master, next_page_callback):
        super().__init__(master)
        self.next_page_callback = next_page_callback

        # create the canvas
        self.canvas = tk.Canvas(root, width=1000, height=600)
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

        self.canvas.create_text(500, 200, text="< JS to Mips Compiler!>", font=('Arial', 50), fill='white', anchor=tk.CENTER)

        # add the button windows to the canvas
        self.button1_window = self.canvas.create_window(250, 360, anchor='nw', window=self.button1)
        self.button2_window = self.canvas.create_window(500, 360, anchor='nw', window=self.button2)

    def next_page(self):
        self.next_page_callback()
    
    def choose_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)

class PageTwo(tk.Frame):
    def __init__(self, master, prev_page_callback):
        super().__init__(master, width=1000, height=600)
        self.prev_page_callback = prev_page_callback

        # Create the widgets for the second page
        self.button_style = {'background': '#007bff', 'foreground': 'white', 'font': ('Arial', 14)}

        # Create a frame to hold the input text and line numbers
        input_frame = tk.Frame(self)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the line number text widget for input
        self.line_numbers_input = tk.Text(input_frame, width=3, bg='grey', fg='white', bd=0, padx=4, pady=4)
        self.line_numbers_input.pack(side=tk.LEFT, fill=tk.Y)

        # Create the input text widget
        self.input_text = tk.Text(input_frame, width=45, height=40, bg='black', fg='white', bd=0, padx=4, pady=4)
        self.input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Link the scrolling of the line numbers and input text widgets
        self.line_numbers_input.config(yscrollcommand=self.input_text.yview)
        self.input_text.config(yscrollcommand=self.line_numbers_input.yview)

        # Create a frame to hold the output text and line numbers
        output_frame = tk.Frame(self)
        output_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the line number text widget for output
        self.line_numbers_output = tk.Text(output_frame, width=3, bg='grey', fg='white', bd=0, padx=4, pady=4)
        self.line_numbers_output.pack(side=tk.LEFT, fill=tk.Y)

        # Create the output text widget
        self.output_text = tk.Text(output_frame, width=50, height=37)
        self.output_text.pack(side=tk.LEFT, padx=5, pady=10, fill=tk.BOTH, expand=True)

        # Link the scrolling of the line numbers and output text widgets
        self.line_numbers_output.config(yscrollcommand=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.line_numbers_output.yview)

        # Create the compile and back buttons
        self.prev_button = tk.Button(self, text="Back", command=self.prev_page, **self.button_style)
        self.prev_button.pack(side=tk.BOTTOM, padx=10, pady=50)

        self.compile_button = tk.Button(self, text="Compile", command=self.compile_code, **self.button_style)
        self.compile_button.pack(side=tk.TOP, padx=10, pady=100)

        # Set up the line numbers for the input text widget
        self.line_numbers_input.insert(tk.END, '1')
        self.input_text.bind('<Return>', self.update_line_numbers_input)
        self.input_text.bind('<BackSpace>', self.update_line_numbers_input)
        self.input_text.bind('<Control-Return>', self.add_newline)

        
        self.output_text.bind('<Return>', self.update_line_numbers)
        self.output_text.bind('<BackSpace>', self.update_line_numbers)
        self.output_text.bind('<Control-Return>', self.add_newline_output)

        # Set up the line numbers for the output text widget
        self.line_numbers_output.insert(tk.END, '1')

    def update_line_numbers_input(self, event=None):
        # Delete the current line numbers for input text
        self.line_numbers_input.delete('1.0', tk.END)

        # Get the number of lines in the input text widget
        num_lines = self.input_text.index(tk.END).split('.')[0]

        # Insert the line numbers for each line in the input text widget
        for line_num in range(1, int(num_lines) + 1):
            self.line_numbers_input.insert(tk.END, str(line_num) + '\n')

    def update_line_numbers(self, event=None):
        # Delete the current line numbers
        self.line_numbers_output.delete('1.0', tk.END)

        # Get the number of lines in the input text widget
        num_lines = self.output_text.index(tk.END).split('.')[0]

        # Insert the line numbers for each line in the input text widget
        for line_num in range(1, int(num_lines) + 1):
            self.line_numbers_output.insert(tk.END, str(line_num) + '\n')

    def add_newline(self, event=None):
        # Add a newline character to the input text widget and update the line numbers
        self.input_text.insert(tk.INSERT, '\n')
        self.update_line_numbers()
    def add_newline_output(self, event=None):
        # Add a newline character to the input text widget and update the line numbers
        self.output_text.insert(tk.INSERT, '\n')
        self.update_line_numbers()

    def prev_page(self):
        self.prev_page_callback()

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

        root.geometry("1000x600")
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
