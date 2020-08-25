import re
f = open('pratyaksh.txt', 'r')

operators = {'=': 'Assignment Operator', '+': 'Additon Operator', '-': 'Substraction Operator', '/': 'Division Operator', '*': 'Multiplication Operator', '++': 'increment Operator', '--': 'Decrement Operator'}
optr_keys = operators.keys()

comments = {r'//': 'Single Line Comment', r'/*': 'Multiline Comment Start', r'*/': 'Multiline Comment End', '/**/': 'Empty Multiline comment'}
comment_keys = comments.keys()

datatype = {'int': 'Integer', 'float': 'Floating Point', 'char': 'Character', 'long': 'long int'}
datatype_keys = datatype.keys()
end_prog = ['$']



special_symbols = ['_', '-', '+', '/', '*', '`', '~', '!', '@', '#', '%', '^', '&', '*', '(', ')', '=', '|', '"', ':', ';', '{' , '}', '[', ']', '<', '>', '?', '/']

numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

dataFlag = False

i = f.read()

count = 0
program = i.split('\n')

for line in program:
    count = count + 1
    print("Line #", count, "\n", line)

    tokens = line.split(' ')
    print("Tokens are", tokens)
    print("Line #", count, 'properties \n')
    for token in tokens:

        if '\r' in token:
            position = token.find('\r')
            token = token[:position]

        if token in optr_keys:
            print("Operator is: ", operators[token])

        if token in comment_keys:
            print("Comment Type: ", comments[token])

        if dataFlag == True and (token not in special_symbols) and ('()' not in token):
            print("Identifier: ", token)

        if token in datatype_keys:
            print("type is: ", datatype[token])
            dataFlag = True

        if '#' in token:
            match = re.search(r'#\w+', token)
            print("Header", match.group())

        if token in numerals:
            print(token, type(int(token)))


    dataFlag = False

    print("________________________")

f.close()