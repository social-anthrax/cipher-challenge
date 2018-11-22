
import codecs
import math
from pycipher import Affine  # gets the affine cipher system
# reads and parses file
text = codecs.open("code.txt", encoding='utf-8').read()
printFile = codecs.open("code2.txt", "w", encoding='utf-8')
text = text.upper()
newText = ""
i = 0


def splitter(n, s):
    pieces = s.split()
    return (" ".join(pieces[i:i + n]) for i in xrange(0, len(pieces), n))


quintiplets = []


quintiplets = text.split(' ')
for i in range(0, len(quintiplets) / 14):
    for columnNum in range(0, 14):
        newText += quintiplets[columnNum * 14 + i] + " "
print(newText)
printFile.write(newText)
