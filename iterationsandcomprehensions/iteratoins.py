f = open('script2.txt').read()
# print(f)

# using the iterations calls to traverse files

f = open('script2.txt')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())  # prints blank string
print(f.readline())

g = open('script2.txt')
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())  this line will raise a exception as it will

h=open('script2.txt')
print(next(h))   # same as __next__()

# other built in iterators
d={'a':1,'b':2,'c':3}
I=iter(d)
print(next(I))
print(next(I))


e= enumerate('Sapam')
i=iter(e)
print(i.__next__())
