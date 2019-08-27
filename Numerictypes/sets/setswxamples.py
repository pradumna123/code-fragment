# working with sets
print("*** working with sets ***")

x=set('abcde')
y=set('bdxyz')
print("two sets are",x,y)


D={1,2,3,4,5,6} # set literals cnoot be emptty else it will be dictionary type

# utilities in expression form   (require both sides to be sets)
print(x-y)   #difference

print(x|y) # union

print(x^y)  # symmetric difference

print(x&y)  # intersection


print(x>y,x<y)  # Superset, subset


# membership tests

print("e in x : ",'e' in x)

# methods along for utilities

z=x.intersection(y)  # intersection
print(z)


z.add('SPAM')    # adding a element
print(z)

z.update(set(['X','Y']))  # Merge: in place union
print("update ",z)


z.remove('b') #delete a item
print("deleting a item",z)

#iterable conainers

for item in set('abc'):
    print(item*3)



#method form of utilities where the other  side can be list


S=set([1,2,3])

# print(S|[3,4]) --> not aloowed with expression

print(S.union([3,4]))

print(S.intersection((1,3,5)))

print(S.issubset(range(-5 ,5)))



#set comprehension


print({x**2 for x in [1,2,3,4]}) # set comprehensions in curly braces same like list comprehensions

#examples of set operation


engineers={'bob','sue','ann','vic'}
managers={'tom','sue'}


print('bob' in engineers)

print(engineers & managers)

print(engineers|managers)

print(engineers-managers)
print(engineers>managers)

