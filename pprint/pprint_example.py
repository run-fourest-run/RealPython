import pprint

stuff = ['alexander','joe','anthony','christopher','David B','David Meeker']
tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',('parrot', ('fresh fruit',))))))))

#showing Indent... Don't feel like this actually did anything
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(stuff)

#showing width ... This deff changed the printed output
pp = pprint.PrettyPrinter(width=4)
pp.pprint(stuff)

#showing depth .. something to note is that if the depth is too deep (...) will be printed)
pp = pprint.PrettyPrinter(depth=2)
pp.pprint(tup)