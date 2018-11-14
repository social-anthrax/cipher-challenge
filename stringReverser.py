import codecs

text = codecs.open("code.txt", encoding='utf-8').read()
printFile = codecs.open("answer.txt", "w", encoding='utf-8')
text = text.upper()


printFile.write(text[:: -1])
