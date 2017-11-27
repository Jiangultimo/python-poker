# python 中的 for 遍历语法位 for in
words = ['cat', 'window', 'defenestrate']
#for w in words:
#print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(1, w)
print(words)