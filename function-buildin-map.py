__author__ = 'mohanchintamanapinna'
###As you can see below , f() and g() do exactly the same and can be used in the same ways.
# Note that the lambda definition does not include a "return" statement -- it always contains an expression which is returned.
# Also note that you can put a lambda definition anywhere a function is expected, and you don't have to assign it to a variable at all.
def f (x): return x**2
print f(8)
g = lambda x: x**2
print g(8)


# An input list.
items = [1, 2, 3]

# Apply lambda to all elements with map.
for r in map(lambda x: x * x, items):
    print(r)
