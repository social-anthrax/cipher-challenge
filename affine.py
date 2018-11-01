import codecs
from pycipher import Affine  # gets the affine cipher system
# reads and parses file
text = codecs.open("code2.txt", encoding='utf-8').read()
printFile = codecs.open("A2.txt", "w", encoding='utf-8')
text = text.upper()
newText = ""

for av in range(0, 25):
    for bv in range(0, 25):
        try:
            # the affine cypher works by the system of c=(p*a + b) mod m and  alphabet of size m are first mapped to the integers in the range 0 … m − 1
            # the deceyption works by the system of E(x)=(a^-1)(x-b) mod b where x is the plaintext index of the alphabet
            newText = Affine(a=av, b=bv).decipher(text, keep_punct=True)

            # just the 3 most common words in the english language
            if "THE" in newText and "BE" in newText and "TO" in newText:
                printFile.write(newText + "\n" + "\n")
        except:
            None
