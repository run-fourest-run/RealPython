'''
The Python Boolean Type:

either:
True||False



High level notes:

* The type Bool is built in, meaning it's always available in Python and doesn't need to be imported.
However, the name itself isn't a keyword in the language.


for example you could do this:

bool = 'see how you can assign to bool'
print(bool)



'''


def see_type_True(var=True):
    print(type(var))

def see_type_False(var=True):
    print(type(var))


see_type_False()
see_type_True()




'''

Below is an exmaple of truthiness. This referes to the boolean evaluation of a value. The Truthiness of a value indicates whether
the value is truthy or falsy. 

'''

def get_Truthiness(obj):
    return bool(obj)



testlist_empty = []
testlist_full = ['this','has','elements']
teststring_empty = ''
teststring_full = 'this is a full string'


print('bool val of an empty list: {}'.format(get_Truthiness(testlist_empty)))
print('bool val of a full list: {}'.format(get_Truthiness(testlist_full)))
print('bool val of an empty string: {}'.format(get_Truthiness(teststring_empty)))
print('bool val of a string with charachters: {}'.format(get_Truthiness(teststring_full)))






def compare_Objects(obj_a,obj_b):
    if bool(obj_a) is True & bool(obj_b) is True:
        print('They both True Dawg')
    else:
        print('Something is off...')


compare_Objects(teststring_full,testlist_full)

