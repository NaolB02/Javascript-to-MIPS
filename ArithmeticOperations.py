from pyjsparser import parse

operations = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'div'
}

def arithmetic_converter(ast, num = 0):

    if ast['type'] == 'Literal':
        stmt = f"add $t{num}, $zero, {ast['raw']}\n"
        return stmt
    
    elif ast['type'] == 'Identifier':
        varname = ast['name']
        

    elif ast['type'] == 'BinaryExpression':
        operator = operations[ast['operator']]
        left = ast['left']
        left = arithmetic_converter(left, num)
        num += 1
        right = ast['right']
        right = arithmetic_converter(right, num)   

        stmt = f"{left}{right}{operator} $t{num - 1}, $t{num - 1}, $t{num}\n"
        num -= 1
        return stmt



js = '''
a > 5
'''
ast= parse(js)
print(ast)
# Generate MIPS assembly code
# code = arithmetic_converter(ast)

# # Print MIPS assembly code
# print(code)


# ast = {'type': 'BinaryExpression', 'operator': '+', 'left': {'type': 'BinaryExpression', 'operator': '+', 'left': {'type': 'Literal', 'value': 9.0, 'raw': '9'}, 'right': {'type': 'Literal', 'value': 4.0, 'raw': '4'}}, 'right': {'type': 'Literal', 'value': 6.0, 'raw': '6'}}
# code = arithmetic_converter(ast)
# print(code)

# ast = {'type': 'BinaryExpression', 'operator': '+', 'left': {'type': 'BinaryExpression', 'operator': '-', 'left': {'type': 'Literal', 'value': 9.0, 'raw': '9'}, 'right': {'type': 'Literal', 'value': 3.0, 'raw': '3'}}, 'right': {'type': 'BinaryExpression', 'operator': '/', 'left': {'type': 'Literal', 'value': 4.0, 'raw': '4'}, 'right': {'type': 'Literal', 'value': 6.0, 'raw': '6'}}}
# ast = {'type': 'BinaryExpression', 'operator': '+', 'left': {'type': 'Literal', 'value': 9.0, 'raw': '9'}, 'right': {'type': 'BinaryExpression', 'operator': '/', 'left': {'type': 'Literal', 'value': 4.0, 'raw': '4'}, 'right': {'type': 'Literal', 'value': 6.0, 'raw': '6'}}}
ast = {'type': 'BinaryExpression', 'operator': '+', 'left': {'type': 'BinaryExpression', 'operator': '-', 'left': {'type': 'BinaryExpression', 'operator': '+', 'left': {'type': 'Literal', 'value': 9.0, 'raw': '9'}, 'right': {'type': 'Literal', 'value': 2.0, 'raw': '2'}}, 'right': {'type': 'Literal', 'value': 3.0, 'raw': '3'}}, 'right': {'type': 'BinaryExpression', 'operator': '*', 'left': {'type': 'Literal', 'value': 4.0, 'raw': '4'}, 'right': {'type': 'Literal', 'value': 6.0, 'raw': '6'}}}
code = arithmetic_converter(ast)
print(code)