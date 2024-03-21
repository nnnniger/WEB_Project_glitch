import pymorphy3

word = 'баня'
morph = pymorphy3.MorphAnalyzer() # морфологический анализатор
p = morph.parse(word)[0]
print(p.tag)
print("noun".upper() in p.tag)