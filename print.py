# print() prints nothing
print()

#Simple Print
print('Welcome to Python101')

#Double quote print
print("Python language's core philosophy is summarized in the document The Zen of Python")

#Print with variable
sample_string ='Python'
print(sample_string)

#Print Tree
print('   o')
print('  o o')
print(' o o o')
print('o o o o')
print('   | ')

#Print variable added to string
sample_name = 'UTD'
print('I am studying @',sample_name)            #note the space is there when , is used
print('I am studying @'+sample_name)            #while concatination space is not there.


a = 5
print("a =", a)                                 # Two objects are passed
b = a
print('a =', 'b =', b)                          # Three objects are passed

print('a','b',b,sep='=')                        # Separator is '=' between objects
print("a =", a, sep='00000', end='\n')          # Separator is '00000' between objects and end ='\n' inserts line break
print("a =", a, sep='0', end=' ')               # Including end='' keeps output on same line
print('= b')

#A new line can also be output by inserting \n.
print('3\n2\n1\nGO!!!')
print('a is', a, '\nb is', b)

print('3 2 1 Go!')                              #prints on single line.

#Arithmetic operation in print
int_one = 2
int_two = 3
print(int_one+int_two)
print('sum is ',int_one+int_two)

# Placeholder %d and %s
print('int_one is',int_one,'\nint_two is',int_two)

print('int_one is %d\nint_two is %d'%(int_one,int_two))             #More readable.


python_inventor='Guido van Rossum'
appeared_year = 1990
print('Python was invented by %s and first appeared in %d'%(python_inventor,appeared_year))


