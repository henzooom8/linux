name = 'World'
more_names = 'Worldly'
line = '+' + name + '+'
spaces = ''

print(line)

for _ in name:
    spaces += 'x'
    print(spaces)

for char in more_names:
    print(spaces)

print(line)