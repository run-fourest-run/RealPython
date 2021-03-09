


'''
Why would I do this?

You might naturally wonder why anybody would want this. Well, sometimes you want to write a .py file that can be both used by other programs and/or modules as a module, and can also be run as the main program itself. Examples:

Your module is a library, but you want to have a script mode where it runs some unit tests or a demo.

Your module is only used as a main program, but it has some unit tests, and the testing framework works by importing .py files like your script and running special test functions. You don't want it to try running the script just because it's importing the module.

Your module is mostly used as a main program, but it also provides a programmer-friendly API for advanced users.
'''
print('before testFunction')
def testFunction():
    print('Test function ')


