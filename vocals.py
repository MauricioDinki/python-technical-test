text = input('Insert a text: ')
vocals_count = 0
transformed_text = ""
for char in text:
    if char is 'a':
        char = 'e'
        vocals_count += 1
    elif char is 'A':
        char = 'E'
        vocals_count += 1
    elif char is 'e':
        char = 'i'
        vocals_count += 1
    elif char is 'E':
        char = 'I'
        vocals_count += 1
    elif char is 'i':
        char = 'o'
        vocals_count += 1
    elif char is 'I':
        char = 'O'
        vocals_count += 1
    elif char is 'o':
        char = 'u'
        vocals_count += 1
    elif char is 'O':
        char = 'U'
        vocals_count += 1
    elif char is 'u':
        char = 'a'
        vocals_count += 1
    elif char is 'U':
        char = 'A'
        vocals_count += 1
    transformed_text += char

print("Vocals Count: %i" % vocals_count)
print("Text: %s" % text)
print("Transformed Text: %s" % transformed_text)
