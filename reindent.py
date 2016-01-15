
import string
def reindent(s, numSpaces):
    s = string.split(s, '\n')
    s = [(numSpaces * ' ') + string.lstrip(line) for line in s]
    s = string.join(s, '\n')
    return s

global x
x= """line one
    line two
    and line three
    """

print (x)

print(reindent(x,5))
