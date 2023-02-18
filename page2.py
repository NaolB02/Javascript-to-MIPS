import tkinter as tk
from pyjsparser import parse

# Create the main window
root = tk.Tk()

root.geometry("800x600")
root.title("JavaScript to MIPS Compiler")

button_style = {'background': '#007bff', 'foreground': 'white', 'font': ('Arial', 14)}


# Create the input text area
input_text = tk.Text(root, width=50, height=40, bg='black', fg='white')
input_text.pack(side=tk.LEFT, padx=10, pady=10)



def compile_code():
    # Get the input code from the text area
    code = input_text.get("1.0", "end-1c")

    # Parse the input code
    parsed_code = parse(code)

    # Generate the MIPS code from the parsed code
    mips_code = generate_mips(parsed_code)

    # Execute the generated MIPS code and capture the output
    result = mips_code

    # Display the output in the output text area
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

compile_button = tk.Button(root, text="Compile", command=compile_code, **button_style)
compile_button.pack(side=tk.BOTTOM, padx=10, pady=10)

# Create the output text area
output_text = tk.Text(root, width=80, height=37)
output_text.pack(side=tk.LEFT, padx=10, pady=10)
# lex()

# Start the main event loop
root.mainloop()

'''
    class PageTwo(tk.Frame):
    def __init__(self, master, prev_page_callback):
        super().__init__(master, width=800, height=600)
        self.prev_page_callback = prev_page_callback

        # Create the widgets for the second page
        self.button_style = {'background': '#007bff', 'foreground': 'white', 'font': ('Arial', 14)}

        # Create a frame to hold the input text and line numbers
        input_frame = tk.Frame(self)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the line number text widget for input text
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

        # Create the line number text widget for output text
        self.line_numbers_output = tk.Text(output_frame, width=3, bg='grey', fg='white', bd=0, padx=4, pady=4)
        self.line_numbers_output.pack(side=tk.LEFT, fill=tk.Y)

        # Create the output text widget
        self.output_text = tk.Text(output_frame, width=50, height=37)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Link the scrolling of the line numbers and output text widgets
        self.line_numbers_output.config(yscrollcommand=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.line_numbers_output.yview)

        # Create the compile and back buttons
        self.prev_button = tk.Button(self, text="Back", command=self.prev_page, **self.button_style)
        self.prev_button.pack(side=tk.BOTTOM, padx=1, pady=20)

        self.compile_button = tk.Button(self, text="Compile", command=self.compile_code, **self.button_style)
        self.compile_button.pack(side=tk.BOTTOM, padx=0, pady=20)

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
'''