name = input("What is your name? ")
print("Hello ", name, "Welcome!")

#printing variables
s = "Anjelina"
age = 25
city = "New York"
print(s, age, city)

#multiple input in python
x, y = input("Enter two values > ").split()
print("X is ", x)
print("Y is ", y)

x,y,z = input("Enter three values > ").split()
print("X is ", x)
print("Y is ", y)
print("Z is ", z)

#print str, int type
n = input("What color is rose? ")
print("Rose is ", n)

o = int(input("How old are you? "))
print("Your age is ", o)

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3, "Geeks":3}
g = dict(f)

print(type(a), 'for String (text)')
print(type(b), 'for integer (numbers')
print(type(b), 'for integer (numbers')
print(type(c), 'for float (decimals)')
print(type(d), 'for tuple. Stores collection of data. cant be changed thus memory-efficient')
print(type(e), 'for list. The same as tuple, but can be changed on run')
print(type(f), 'for dictionary. Collections of key:value pairs that are ordered, changeable and do not allow duplicates.')