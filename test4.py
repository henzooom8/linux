sentence = 'heLlo WorlD!'
letter = ''
capital = True

for char in sentence:
    if capital:
        char = char.upper()
    else:
        char = char.lower()
    letter += char
    capital = False

print(letter)

