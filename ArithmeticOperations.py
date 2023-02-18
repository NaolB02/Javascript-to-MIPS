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

