from pyjsparser import parse

js_code = 'console.log("hello world")'
ast = parse(js_code)

print(ast)