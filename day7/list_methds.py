letters = ['a','b','c','d','y','f','v']

print(len(letters))

letters.extend(['x','f','z'])
print(letters,"after extend")

letters.insert(1,'r')
print(letters, 'after insert')

letters.remove('r')
print(letters, 'after remove')

print(letters.pop(2))
print(letters, 'after pop')

letters.sort()
print(letters,"after sort")

print(letters.index('x'))

letters.reverse()
print(letters,"after reverse")