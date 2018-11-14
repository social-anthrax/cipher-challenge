import codecs

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
text = codecs.open("code.txt", encoding='utf-8').read()
printFile = codecs.open("answer.txt", "w", encoding='utf-8')
text = text.upper()
newText = ""

for shift in range(0, 25):
    newText = ""
    for char in text:
        if char in alphabet:
            loc = (alphabet.index(char)) + shift
            if loc > 25:
                loc = loc - 26
            newText += alphabet[loc]
        else:
            newText += char

    # if "THE" in newText:
    printFile.write(newText)
