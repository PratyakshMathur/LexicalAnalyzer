import re
print("1: click f for making file as input"
 "2: click i for entering your input")
f = open('Filename', 'r')
i = f.read()
number={'1': 'one','2': 'Two','3': 'Three','4': 'Four','5': 'FIve','6': 'Six','7': 'Seven','8': 'Eight','9':'Nine','0': 'Zero', }
number_keys=number.keys()
operators = {'=': 'Assignment Operator', '+': 'Additon Operator', '-': 'Substraction Operator', '/': 'DivisionOperator', '*': 'Multiplication Operator', '++': 'increment Operator', '--': 'Decrement Operator'}
optr_keys = operators.keys()
count = 0
program = i.splitlines()
b=input()
if b == 'f':
 for element in program:
 count = count + 1
 print("###Line####", count, "\n", element)
 tokens = element.split(' ')
 print("Tokens is/are", tokens)
 print("elements ", 'property \n')
 for token in tokens:
 if token in optr_keys:
 print("Element is: ", operators[token])
 elif token in number_keys:
 print("Element is: ", number[token])
 else:
 print("Elemnt is a String or not an operator :", token)
if b == 'i':
 a=input("please enter your token one by one :")
 if a in optr_keys:
 print("Element is: ", operators[a])
 elif a in number_keys:
 print("Element is: ", number[a])
 else :
 print("Elemnt is a String or not an operator :", a)
