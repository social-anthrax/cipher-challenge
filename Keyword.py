import codecs
import string
# reads and parses file
text = codecs.open("code.txt", encoding='utf-8').read()
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
modAlphabet = ""
wordBank = codecs.open("words.txt", encoding='utf-8').read()
wordBank = wordBank.upper()
printFile = codecs.open("answer.txt", "w", encoding='utf-8')
text = text.upper()
newText = ""


def MakeAlphabet(word):

    # removes the last occurances of repeating letters
    tempword = ""
    for i in word:
        tempword = i + tempword
    for i in tempword:
        while tempword.count(i) > 1:
            tempword = tempword.replace(i, "", 1)
    word = ""
    for i in tempword:
        word = i + word

    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    new = word

    while len(new) < 26:
        for i in alphabet:
            if i not in word:
                new = new + i
    return new


# wordBank = "".join(c for c in wordBank if c not in ('!', '.', ':', ',', '’'))
for word in wordBank.split():
    newText = ""
    # word = "loyatz".upper()
    modAlphabet = MakeAlphabet(word)
    # print(modAlphabet)
    for char in text:
        if char in modAlphabet:

            print(char)
            loc = (modAlphabet.index(char))
            print(loc)
            newText += alphabet[loc]
        else:
            newText += char
    # if "HER MA" in newText:

    printFile.write(modAlphabet + "\n" + alphabet + "\n" + "\n" +
                    newText + "\n" + "------------------------------" + "\n")
