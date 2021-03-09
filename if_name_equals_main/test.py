
'''
High level explination of "if __name__ == "__main__":"
as found on: https://stackoverflow.com/questions/419163/what-does-if-name-main-do


Somethings to know: Whenever the python interpreter reads a source file it does two things:

* sets some special variables like __name__,
* executes all the code found in the file


Special Variables:

* in this particular instance when the python interpreter reads a source file, it defines
a few special variables --> in this case we obviously care about __name__




# if you are running the module (source file) as the main program e.g:

---

python test.py
---

the interpretter will assign the hard coded string "__main__" to the __name__ variable:
in other words ..
__name__ = "__main__"





# On the other hand if some other module is the main program and it imports your module.
This means there's a statement like this in the main program, or some other module the main imports


The interpreter will search for your test.py file (along with searching for a few other variants) and prior
to executing that module, it will assign the name 'test' from the import statement to the __name__ variable

__name__ = 'test'








Executing the module (again a module is source code):
* Once the variables are set the interpretor executes all the code in the module.
*


Always

It prints the string "before import" (without quotes).

It loads the math module and assigns it to a variable called math. This is equivalent to replacing import math with the following (note that __import__ is a low-level function in Python that takes a string and triggers the actual import):

# Find and load a module given its string name, "math",
# then assign it to a local variable called math.
math = __import__("math")
It prints the string "before functionA".

It executes the def block, creating a function object, then assigning that function object to a variable called functionA.

It prints the string "before functionB".

It executes the second def block, creating another function object, then assigning it to a variable called functionB.

It prints the string "before __name__ guard".











'''



print('before import')
import math


print('before functionA')
def functionA():
    print('Function A')

print('before functionB')
def functionB():
    print('Function B {}'.format(math.sqrt(100)))

print('before __name__ guard')
if __name__ == "__main__":
    functionA()
    functionB()
    print('after __name__ guard')