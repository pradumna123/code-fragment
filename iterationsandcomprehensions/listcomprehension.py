l = [1, 2, 3, 4, 5]

for i in range(len(l)):
    l[i] += 10

print(l)

l = [x + 100 for x in l]
print(l)

# using list comprehension on files

f = open('script2.txt')
lines = f.readlines()
print(lines)

line = [line.upper() for line in lines]
print(line)

line = [line.rstrip() for line in open('script2.txt') if line[0] == 'p']  # using if clause in list comprehension
print(line)

a = [x + y for x in 'abc' for y in "ymn"]  # nested loops
print(a)

b = list(zip(open('script2.txt'), open('script2.txt')))
print(b)


