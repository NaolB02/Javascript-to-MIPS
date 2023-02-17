import pyjsparser
from pyjsparser import parse


def while_to_mips(js_code):
    # Parse the JavaScript code using Pyjsparser
    ast = pyjsparser.parse(js_code)

    # Find the while loop in the AST
    while_stmt = next(stmt for stmt in ast['body'] if stmt['type'] == 'WhileStatement')

    # Extract the loop condition, incrementer and body
    cond = while_stmt['test']
    incrementer = None
    for stmt in while_stmt['body']['body']:
        if stmt['type'] == 'UpdateExpression':
            incrementer = stmt
            break
    body = ''

    # Generate MIPS code for the loop
    mips_code = []

    # Evaluate the loop condition
    def eval_cond(node):
        if node['type'] == 'Identifier':
            mips_code.append(f"lw $t0, {node['name']}")
        elif node['type'] == 'Literal':
            mips_code.append(f"li $t0, {node['value']}")
        elif node['type'] == 'BinaryExpression':
            left = node['left']
            right = node['right']
            eval_cond(left)
            mips_code.append(f"sw $t0, 0($sp)")
            mips_code.append(f"addiu $sp, $sp, -4")
            eval_cond(right)
            mips_code.append(f"lw $t1, 4($sp)")
            mips_code.append(f"addiu $sp, $sp, 4")
            op = node['operator']
            if op == '<':
                mips_code.append(f"blt $t1, $t0, eval_true")
            elif op == '<=':
                mips_code.append(f"bgt $t1, $t0, eval_false")
            elif op == '>':
                mips_code.append(f"bgt $t1, $t0, eval_true")
            elif op == '>=':
                mips_code.append(f"blt $t1, $t0, eval_false")
            elif op == '==':
                mips_code.append(f"bne $t1, $t0, eval_false")
            elif op == '!=':
                mips_code.append(f"beq $t1, $t0, eval_false")
        else:
            raise ValueError(f"Unsupported loop condition type: {node['type']}")

    eval_cond(cond)

    # Loop start label
    loop_start_label = f"loop_start_{id(while_stmt)}"
    mips_code.append(f"{loop_start_label}:")
    
    # Test the loop condition and exit if false
    mips_code.append("eval_false:")
    mips_code.append("beq $t0, $zero, loop_end")
    mips_code.append("eval_true:")

    # Generate MIPS code for the loop body
    if body:
        body_mips = [] # call haile's code here
        mips_code.extend(body_mips)

    # Generate MIPS code for the loop incrementer
    if incrementer:
        incrementer_mips = [] # call naol's code here
        mips_code.extend(incrementer_mips)

    # Go back to the start of the loop
    mips_code.append(f"j {loop_start_label}")

    # Loop end label
    mips_code.append("loop_end:")

    # Return the generated MIPS code
    return mips_code


def for_to_mips(js):
    try:
        mips = ""
        js_ast = parse(js)

        # print(js_ast)

        the_body = js_ast['body']
        loop_var = js_ast['body'][0]['init']['declarations'][0]['id']['name']
        loop_start = js_ast['body'][0]['init']['declarations'][0]['init']['value']
        loop_end = js_ast['body'][0]['test']['right']['value']

        mips += f"li $t0, {loop_start}\n"
        mips += f"li $t1, {loop_end}\n"
        mips += f"li $t2, 1\n"
        mips += f"loop_start:\n"
        mips += f"beq $t0, $t1, loop_end\n"

        for node in the_body:
            if node['type'] == "If":
                mips += ""  # hailes code

        mips += f"addi $t0, $t0, $t2\n"
        mips += f"j loop_start\n"
        mips += f"loop_end:\n"
        return mips

    except SyntaxError as e:
        print(f"Error parsing JavaScript code: {e}")
        return None


js_code = "for(let i = 0; i <= 15; i++){}"


def loop_to_mips(js_code):
    # Parse the JavaScript code using Pyjsparser
    ast = pyjsparser.parse(js_code)

    # Look for a for loop or a while loop in the AST
    for_stmt = next(
        (stmt for stmt in ast['body'] if stmt['type'] == 'ForStatement'), None)
    while_stmt = next(
        (stmt for stmt in ast['body'] if stmt['type'] == 'WhileStatement'), None)

    # If neither loop is found, raise an error
    if not for_stmt and not while_stmt:
        raise ValueError(
            "The code does not contain a for loop or a while loop.")

    # If a for loop is found, convert it to MIPS
    if for_stmt:
        return for_to_mips(js_code)

    # If a while loop is found, convert it to MIPS
    if while_stmt:
        return while_to_mips(js_code)


mips_code = loop_to_mips(js_code)
print(mips_code)

second_js_code = """
let i = 0;
while (i < 10) {
  
}
"""

# Convert the while loop to MIPS
mips_code = while_to_mips(second_js_code)

# print(mips_code)
# Print the generated MIPS code
for line in mips_code:
    print(line)


print("--------------------------------------------------------------------------------------------------------------------")


print(for_to_mips(js_code))