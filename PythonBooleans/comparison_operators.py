'''
Equality Operators will return either True or False

==  : Equality Operator
==  : Inequality Operator




'''

equality_test_booleans1 = 1 == 1
equality_test_booleans2 =  1 == 2
equality_test_booleans3 = 1 == 1.0


def print_equality_booleans(eq_test_bool1,eq_test_bool2,eq_test_bool3):
    print('equality test 1 = {};'.format(eq_test_bool1),'equality test 2 = {};'.format(eq_test_bool2),'equality test3 = {};'.format(eq_test_bool3))




'''
Order  Comparisons


Another set of test operators are the order comparison operators. These are the four order comparison operators:

The order comparison operators can be categorized as the following: Direction, Strictness


Strict, Less Than : <
Strict, Greater Than : >
Not Strict, Less Than: <=
Not Strict, Greater Than: >=

Resulting in a total of four order comparison operators: 





'''

test_dict_a = {1:5}
test_dict_b = {1:5}
test_list_a = [1,5]
test_list_b = [1,5]
test_string_a = 'one,five'

def test_order_Comparison(objA,objB):
    try:
        result = objA > objB
        return 'Object A is greater than Object B: {}'.format(result)
    except TypeError:
        return 'type error occur'


#This should throw an error since you can't use any sort of comparison operators against Dicts
test1 = test_order_Comparison(test_dict_a,test_dict_b)

#This should be fine
test2 = test_order_Comparison(test_list_a,test_list_b)

#This should raise a type error. Can't order compare across types
test3 = test_order_Comparison(test_list_a,test_string_a)

print(test1)
print(test2)
print(test3)

'''
Order Comparison Operators when properly defined should return a boolean Type
'''