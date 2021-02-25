'''
The AND operator:

ex:

<Expression A> and <Expression B>

The python keyword 'and' is used to determine truthiness of two expressions. Basically
it looks to see if the expression to the left and right of the operand are truthy.
If one of the expressions is falsy everything is falsy
'''

list_with_elements = ['this','list','has','elements']
list_empty = []
string_with_elements = 'this string has elements'
string_empty = ''




def using_and_Keyword(obja,objb):
    if obja and objb:
        print('both objects evaluate to True')
    else:
        print('one or more objects evaluates to False')


using_and_Keyword(string_with_elements,list_with_elements)