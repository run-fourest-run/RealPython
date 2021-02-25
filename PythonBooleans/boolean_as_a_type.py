'''
Booleans are considered a numeric type in python:

That means that they evaluate to a numeric number. Not super helpful
but one thing you could use this for is to maybe count the number of 'Truthy' objects.


Source:
https://realpython.com/python-boolean/#the-python-boolean-type

'''



'''
Apparently this is a good example of because True = 1 and False is equal = 0

The number of times True is in the generator is equal to the number of lines that equal 'the'
'''


lines = '''
He took his vorpal sword in hand;
Long time the manxome foe he sought—
So rested he by the Tumtum tree
And stood awhile in thought.
'''.splitlines()



sum_of_word = sum('the' in line.lower() for line in lines) / len(lines)



'''let's split up the code above to see how it works'''



lines = '''
He took his vorpal sword in hand;
Long time the manxome foe he sought—
So rested he by the Tumtum tree
And stood awhile in thought.
'''

lines_split = lines.splitlines()
second_line = lines_split[1]
third_line = lines_split[2]

print(second_line,'\n',third_line)

_evaluate_second_line = 'He' in second_line
_evaluate_third_line = 'He' in third_line

print('this expression should evaulate to {} (Expected True)'.format(_evaluate_second_line))
print('this expression should evaluate to {} (Expected False)'.format(_evaluate_third_line))

test_list = ['the' for line in lines_split]

proportion_of_lines_with_word = sum('the' for line in lines_split) / len(lines_split)




































list1 = ['element']
list2 = ['element']
list3 = ['element']
list4 = ['element']
list5 = ['element']
list6 = ['element']
list7 = ['element']
list8 = []


list_of_lists = []
list_of_lists.append(list1)
list_of_lists.append(list2)
list_of_lists.append(list3)
list_of_lists.append(list4)
list_of_lists.append(list5)
list_of_lists.append(list6)
list_of_lists.append(list7)
list_of_lists.append(list8)










