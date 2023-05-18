

print('Hello, this is a script.')
text = input('What would you like to say?: ')

print('\nThis is the hexadecimal value of what you just input:')
print(text.encode().hex('-'))

print('\nAnd this is binary:')
print(bin(int(text.encode().hex(), base=16)))