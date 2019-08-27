r = range(10)
print(r, type(r))

i = iter(r)
print(i.__next__())
print(i.__next__())
print(i.__next__())