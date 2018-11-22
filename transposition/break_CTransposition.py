# TODO: alphabet is being cut short by columnNum. Make so that alphabet can be put into maxkey


from pycipher import ColTrans as SimpleSub
import random
import re
from ngram_score import ngram_score
import codecs
from math import factorial
# load quadgram statistics
fitness = ngram_score('quadgrams.txt')

ctext = codecs.open("../code.txt", encoding='utf-8').read()
ctext = re.sub('[^A-Z]', '', ctext.upper())
printFile = codecs.open("../answer.txt", "a", encoding='utf-8')

print "Transposition solver, you may have to wait several iterations"
print "for the correct result. Press ctrl+c to exit program."

maxscore = -99e9
for columnNum in range(4, 15, 1):
    print "column length is now " + str(columnNum)
    maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    parentscore, parentkey = maxscore, maxkey[:]
    random.shuffle(parentkey)
    # keep going until we are killed by the user
    i = 0
    for x in range(0, factorial(columnNum)):
        i = i + 1
        random.shuffle(parentkey)
        deciphered = SimpleSub(''.join(parentkey)).decipher(ctext)
        parentscore = fitness.score(deciphered)
        count = 0
        while count < (2 ^ columnNum):
            a = random.randint(0, columnNum - 1)
            b = random.randint(0, columnNum - 1)
            child = parentkey[:]
            # swap two characters in the child
            child[a], child[b] = maxkey[b], maxkey[a]
            child = child[:columnNum]
            deciphered = SimpleSub(''.join(child)).decipher(ctext)
            score = fitness.score(deciphered)
            # if the child was better, replace the parent with it
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count + 1
            # keep track of best score seen so far
            if parentscore > maxscore:
                maxscore, maxkey = parentscore, parentkey[:]
                print '\nbest score so far:', maxscore, 'on iteration', i
                ss = SimpleSub(''.join(maxkey))
                print '    best key: ' + ''.join(maxkey)
                print '    plaintext: ' + ss.decipher(ctext)

                printtext = "\nbest score so far:" + \
                    str(maxscore) + "on iteration" + str(i)
                printFile.write(printtext)
                printtext = '    best key: ' + ''.join(maxkey)
                printFile.write(printtext)
                printtext = '    plaintext: ' + ss.decipher(ctext)
                printFile.write(printtext)
