
import codecs
import math
from pycipher import Affine  # gets the affine cipher system
# reads and parses file
text = codecs.open("code.txt", encoding='utf-8').read()
printFile = codecs.open("answer.txt", "w", encoding='utf-8')
text = text.upper()
newText = ""
i = 0


def splitter(n, s):
    pieces = s.split()
    return (" ".join(pieces[i:i + n]) for i in xrange(0, len(pieces), n))


for x in range(0, int(math.ceil(len(text) / 5))):

    newText += text[(i * 5) + 1:((i + 1) * 5) + 1]
    i += 1
print(newText)
