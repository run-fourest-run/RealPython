'''
Problem:

When to use a for loop vs when to use a while loop. As explained in this thread:
https://www.reddit.com/r/learnpython/comments/lq47a5/in_what_situations_do_you_benefit_from_using_a/


'''





lumber = ['lumber1','lumber2','lumber3','lumber4','lumber5']



def create_str(base:str):
    for _num in range(100):
        full_str = '{}{}'.format(base,_num)
        yield full_str


lumber = []
for x in create_str('lumber'):
    lumber.append(x)

'''
A for loop makes sense when you know the total number of elements to inspect:
Let's say I have a truck full of lumber. I want to pull out twentypieces of lumber.
It doesn't matter how many apples exist in the truck (sequence), but you have a clear understanding
of the number of times you want to perform some action. 
'''


def get_twenty_logs_for_loop(lumber:list):
    first_twenty_logs = list()
    for log in lumber[0:20]:
        first_twenty_logs.append(log)
    return first_twenty_logs


first_twenty_logs = get_twenty_logs_for_loop(lumber)
for x in first_twenty_logs:
    print(x)

'''
Now let's say that I don't know how many I'll need to pick in order to get twenty good ones
'''

while len(apples)< 20:
    apple = pick_apple()
    if not apple.rotten()
        apples.append


