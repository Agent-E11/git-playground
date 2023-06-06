# Introduce yourself
print('Hello, this is a script.')

# Ask a random question
text = input('What would you like to say?: ')

# Respond to their question
print('\nThis is the hexadecimal value of what you just input:')
print(text.encode().hex('-'))

# Respond again
print('\nAnd this is binary:')
print(bin(int(text.encode().hex(), base=16)))