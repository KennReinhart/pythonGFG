'''rules for variables
Variable names can only contain letters, digits and underscores
Cant start with a digit
Variable names are casse-sensitive like myVar and myvar are different
Avoid using python keywords like if, else, for as variable names
'''

import keyword
kwlist = keyword.kwlist
print("The list of keywords are : ")
print(kwlist)