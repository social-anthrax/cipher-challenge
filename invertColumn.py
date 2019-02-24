
import codecs
import math
from pycipher import Affine  # gets the affine cipher system
# reads and parses file
text = codecs.open("code.txt", encoding='utf-8').read()
printFile = codecs.open("answer.txt", mode="w", encoding='utf-8')
text = text.upper()
newText = ""
i = 0
totalColumns = 14


def splitter(n, s):
    pieces = s.split()
    return (" ".join(pieces[i:i + n]) for i in xrange(0, len(pieces), n))


quintiplets = []


quintiplets = text.split(' ')
# print(quintiplets)
for i in range(0, totalColumns):  # len(quintiplets) / totalColumns)
    for columnNum in range(0,  len(quintiplets) / totalColumns):

        # splits up the string into sets of totalColumns amd then finds the number above totalColumns and gets that coulymn row thing. I just wrote this and i dont know how it works.
        newText += quintiplets[columnNum * totalColumns + i] + " "
    # newText += "\n"
print(newText)
printFile.write(newText)
