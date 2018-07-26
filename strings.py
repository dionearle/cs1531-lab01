strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = strings[0]
for i in strings[1:]:
    sentence += ' ' + i
    
print(sentence)
print(' '.join(strings))
