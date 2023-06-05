from pyjsparser import parse
nums = set()
asm = []
dataCtr = 0
varCtr = 0
data = []
expression =[{'type': 'ExpressionStatement', 'expression': {'type': 'AssignmentExpression', 'operator': '=', 'left': {'type': 'Identifier', 'name': 'hello'}, 'right': {'type': 'Literal', 'value': 1, 'raw': "'bro'"}}}, {'type': 'ExpressionStatement', 'expression': {'type': 'CallExpression', 'callee': {'type': 'MemberExpression', 'computed': False, 'object': {'type': 'Identifier', 'name': 'console'}, 'property': {'type': 'Identifier', 'name': 'log'}}, 'arguments': [{'type': 'Identifier', 'name': 'hello'}]}}]

def stdOutput(expression, dataCtr):
    if expression["arguments"][0]["type"]== "Literal":
                val = expression["arguments"][0]["value"]
                strLabel = f"string{str(dataCtr)}"
                dataCtr += 1
                data.append(f'  {strLabel}: .asciiz "{val}"')
                asm.append(f"li $v0,4")
                asm.append(f"la $a0, {strLabel}")
                asm.append("syscall")
                asm.append("")

    elif expression["arguments"][0]["type"]== "Identifier":
        label = expression["arguments"][0]["name"]
        if label in nums:
            asm.append(f"li $v0, 1")
            asm.append(f"lw $a0, {label}")
        else:
            asm.append(f"li $v0,4")
            asm.append(f"la $a0, {label}")
        asm.append("syscall")
        asm.append("")

    elif expression["arguments"][0]["type"]== "BinaryExpression":
        arithmetic_converter(expression["arguments"][0])
        asm.append(f"li $v0, 1")
        asm.append(f"mov $a0, $t0")
        asm.append(f"syscall")

def evalExpression(expression, dataCtr):
    type = expression["type"]
    if type == "CallExpression":
        callee = expression["callee"]
        if callee["object"]["name"] == "console" and callee["property"]["name"]== "log":
            stdOutput(expression, dataCtr)

    elif type == "AssignmentExpression":
        identifier = expression["left"]["name"]
        if expression["right"]["type"] == "Literal":
            val = expression["right"]["value"]
            if isinstance(val, int):
                data.append(f"    {identifier}: .word {val}")
                nums.add(identifier)
            else:
                data.append(f'  {identifier}: .asciiz "{val}"')

        elif expression["right"]["type"] == "BinaryExpression":
            arithmetic_converter(expression["right"])
            data.append(f"    {identifier}: .word")
            asm.append(f"sw $t0, {identifier}")
            asm.append("")

for e in expression:
    evalExpression(e["expression"], dataCtr)

print(".text:")
for line in asm:
    print(f"    {line}")
print(".data:")
for d in data:
    print(d)

