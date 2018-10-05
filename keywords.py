import keyword
import math as myAlias
print('Pi is => ',myAlias.pi)


print(keyword.kwlist)                   #prints the list of all kewwords


# True False
print('1 == 1', 1 == 1)
print('5 > 3', 5 > 3)
print('5 != 7', 5 != 7)
print('10 <= 1', 10 <= 1)
print(' 3 > 7',  3 > 7)

print('a == a', 'a' == 'a')
print('a == b', 'a' == 'b')
print('a != a', 'a' == 'b')
print('b == a', 'b' == 'a')


print('True == 1 is ', True == 1)
print('False == 0 is ', False == 0)


# None

print('None == 0',None == 0)
print('None == []',None == [])
print('None == False',None == False)
x = None
y = None
print('x == y',x == y)



def a_void_function():
    a = 1
    b = 2
    c = a + b


x = a_void_function()
print(x)


def improper_return_function(a):
    if (a % 2) == 0:
        return True
x = improper_return_function(3)
print(x)


#and or not
print('True and False =>', True and False)
print('False and False =>', False and False)
print('True and True =>', True and True)
print('True or False =>',True or False)
print('False or False =>', False or False)
print('not True =>', not True)
print('not False =>', not False)
