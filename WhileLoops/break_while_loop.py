'''
On Previous examples the entire body of the while loop is executed on each iteration.
Python provides two keywords to terminate iteration early:

break:
immediately terminates a loop entirely. Program execution proceeds to the first statement following loop body


continue:
immediately terminates the current loop iteration. Execution jumps to the top of the loop, and the controlling expression
is re-evaluated
'''

# when the conditional break statement is met it breaks the entire loop... outout should just be n - 2n
def demo_break_keyword(n):
    while n > 0:
        n -= 1
        if n == 2:
            break
        print(n)
    print('loop ended')


# when n is encountered it is essentially skipped.
def demo_continue_keyword(n):
    while n < 5:
        n += 1
        if n == 2:
            continue
        print(n)
    print('loop ended')

demo_continue_keyword(0)