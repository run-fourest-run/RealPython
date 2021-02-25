'''
source: https://realpython.com/python-while-loop/


Iteration means executing the same block of code over and over, potentially many times. A Programming structure that implements iteration is caled a loop.


In programming there are two types of iteration: definite and indefinate.

Indefinate iteration: The number of times the loop is executed isn't specified explicitly in advance. Rather the designated block is executed repeatedly as long as some condition is met
Definiate iteration: The number of times the designated block will be executed is specified explicitly at the time the loop starts


Based on that definition it sounds like Indefinite iteration applies to While Loops...



Typically while loop syntax:

    while <Expression>:
        <statement(s)>


controlling <expression> typically involves one or more variables that are intialiazed prior to start of loop
and then modified somewhere in the body of the loop.

<expression> is typically evaluated in a boolean context.

'''


test_list = [x for x in range(5)]
test_int = 4
test_string = 'hey'


def test_basic_while_loop(obj):
    while obj > 0:
        obj -= 1
        print(obj)




def test_basic_while_loop_list(lst_obj):
    while lst_obj:
        print(lst_obj.pop(-1))


'''keep in mind when lists are evaluated in boolean when they are empty they are falsy. So in the above example with pop - every item is removed until there are no items in the list
at which point a StopIteration is raised. '''
test_basic_while_loop_list(test_list)



