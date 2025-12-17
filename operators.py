'''Operators : Special symbols like -, +, *, / , etc
Operands : Value on which the operator is applied'''

a = 15
b = 4

#Arithmetic
print('A = 15 B = 4')
print('Addition =',a+b)
print('Subtraction =',a-b)
print('Multiplication =',a*b)
print('Division =',a/b)
print('Floor division =',a/b)
print('Modulos =',a%b)
print('Power / Exponentiation =',a**b)
print()

#Comparison
a = 13
b = 33

print('a = 13 b = 33')
print('a > b is', a > b)
print('a < b is', a < b)
print('a == b is',a == b)
print('a != b is',a != b)
print('a >= b is',a >= b)
print('a <= b is',a <= b)
print()

#Logical operators

a = True
b = False

print('a is True and b is False')
print('a and b is',a and b)
print('a or b is', a or b)
print('not a is', not a)
print('not b is', not b)
print()

#Bitwise operators

a = 10
b = 4

print('Bitwise AND is a & b ', a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a << b)
print(a >> b)
print()

#Assignment operators

a = 10
b = 4

print(b)
b += a      #addition
print(b)
b -= a      #substraction
print(b)
b *= a      #multiplication
print(b)
b **= a     #exponentiation
print(b)
b //= a     #floor division
print(b)
b %= a      #modulus
print(b)