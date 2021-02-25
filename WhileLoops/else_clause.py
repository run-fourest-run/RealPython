'''
Python allows for else clause at the end of a while loop. This is a unique feature of Python, not found in most other programming langauges. Syntax is below.

Example 1: While look with Else Clause

while <expression>:
    <statements(s)>
else:
    <other statement(s)>



%%%%%%%%%%%%%%
...but how is that different from below
%%%%%%%%%%%%%




Example 2: While loop with additional statement outside of loop

while <expression>:
    <statement(s)>
<other statements>


In Example 2 - if there is no else clause the statement will be executed no matter what.
In Example 1 - When additional statements are placesd in an else clause, they will only be executed if the loop terminates by exhaustion. If the loop exited by a break statement
the else clause won't be executed.






'''


#Example 2
def while_loop_else_Example(n):
    while n < 0:
        n -= 1
        print(n)
    else:
        print('loop done')

def while_loop_else_break_Example(n):
    while n > 0 :
        n -= 1
        print(n)
        if n == 2:
            break
    else:
        print('loop done')







'''example useful else clause - searching a list for a specific item'''



se = ['alexander','joe','anthony','david']
def search_list(list_obj,break_obj):
    i = 0
    while i < len(list_obj):
        if list_obj[i] == break_obj:
            break
        i += 1
    else:
        print('{} not found'.format(break_obj))

test = search_list(se,'joe')
print(test)

