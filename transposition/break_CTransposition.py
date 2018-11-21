
from pycipher import ColTrans as SimpleSub
import random
import re
from ngram_score import ngram_score
import codecs
# load our quadgram statistics
fitness = ngram_score('quadgrams.txt')

ctext = codecs.open("../code.txt", encoding='utf-8').read()
printFile = codecs.open("../answer.txt", "a", encoding='utf-8')

maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
maxscore = -99e9
parentscore, parentkey = maxscore, maxkey[:]
print "Substitution Cipher solver, you may have to wait several iterations"
print "for the correct result. Press ctrl+c to exit program."
# keep going until we are killed by the user
i = 0
while 1:
    i = i + 1
    random.shuffle(parentkey)
    deciphered = SimpleSub(parentkey).decipher(ctext)
    parentscore = fitness.score(deciphered)
    count = 0
    while count < 1000:
        a = random.randint(0, 25)
        b = random.randint(0, 25)
        child = parentkey[:]
        # swap two characters in the child
        child[a], child[b] = child[b], child[a]
        deciphered = SimpleSub(child).decipher(ctext)
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
        ss = SimpleSub(maxkey)
        print '    best key: ' + ''.join(maxkey)
        print '    plaintext: ' + ss.decipher(ctext)

        printtext = "\nbest score so far:" + maxscore + "on iteration" + i
        printFile.write(printtext)
        printtext = '    best key: ' + ''.join(maxkey)
        printFile.write(printtext)
        printtext = '    plaintext: ' + ss.decipher(ctext)
        printFile.write(printtext)


# def decipher(cipher_txt, key):
#     """
#     Deciphers a given cipher text with a key using the transposition
#     cipher
#     """
#     pad_char = "&"
#     # Perform basic normalisation of the inputs
#     key = key.lower()
#     cipher_txt = cipher_txt.upper().replace(" ", "").translate(string.punctuation)
#
#     # remove duplicate characters
#     __key = ""
#     for c in key:
#         if c not in __key:
#             __key += c
#     # Find the order of the key, based on the position of the chars
#     # in the alphabet
#     __key_sorted = sorted(__key)
#     key_order = []
#     for c in __key:
#         key_order.append(__key_sorted.index(c))
#     #logger.debug("Key order for {}: {}".format(key, key_order))
#
#     # split the cipher text based on the length of the key into chunks
#     chunks = []
#     col_length = ceil(len(cipher_txt) / len(key_order))
#     .debug("col length: {}".format(col_length))
#     if len(cipher_txt) % len(key_order) != 0:
#         # Add Null characters where needed
#         placeholders = (col_length * len(key_order)) - len(cipher_txt)
#         ##logger.debug("Placeholders: {}".format(placeholders))
#         indexes_to_add_to = key_order[-placeholders:]
#         #logger.debug("Indexes to add Null chars: {}".format(indexes_to_add_to))
#         for i in sorted(indexes_to_add_to):
#             if i == 0:
#                 cipher_txt = cipher_txt[:col_length - 1] + pad_char + \
#                     cipher_txt[col_length - 1:]
#             else:
#                 cipher_txt = cipher_txt[:i * col_length + col_length - 1] + \
#                     pad_char + cipher_txt[i * col_length + col_length - 1:]
#         #logger.debug("Cipher text after: {}".format(cipher_txt))
#
#     for i in range(len(key_order)):
#         chunks.append(cipher_txt[i * col_length:(i * col_length) + col_length])
#     #logger.debug("Chunks: {}".format(chunks))
#
#     # Order the chunks in the order of the key
#     ordered_chunks = []
#     for pos in key_order:
#         ordered_chunks.append(chunks[pos])
#     #logger.debug("Ordered_chunks: {}".format(ordered_chunks))
#     out = ""
#     for c in range(col_length):
#         for chunk in range(len(ordered_chunks)):
#             # Do inside try/except block as if there aren't nulls at the
#             # end of the cipher text the block lengths won't be the same
#             try:
#                 out += ordered_chunks[chunk][c]
#             except IndexError:
#                 pass
#     #logger.debug("Output: {}".format(out))
#
#     return out.replace(pad_char, "")
