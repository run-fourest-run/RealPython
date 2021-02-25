'''
the 'is' operator checks for identity


the 'is' operator evaluates to true only when x and y evaluate to the same object. It has an opposite operator 'is not'


typically used to compare lists for identity

'''




x = []
y = []


def evaluate_same_object(x,y):
    return 'objects evaluate to the same object: {}'.format(x is y)


eval_x_x = evaluate_same_object(x,x)
eval_x_y = evaluate_same_object(x,y)
eval_y_y = evaluate_same_object(y,y)


print(eval_x_x)
print(eval_x_y)
print(eval_y_y)