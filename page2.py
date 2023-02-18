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