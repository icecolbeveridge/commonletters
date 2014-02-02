from random import choice
from urllib2 import urlopen
f = urlopen( "http://scrapmaker.com/data/wordlists/twelve-dicts/2of4brif.txt")

r = [l.strip() for l in f.readlines()]

yep = 0
nope = 0
TRIALS = 1000000


def commonLetter(w1, w2):
    for ii in w1:
        for jj in w2:
            if ii == jj:
                return True
    return False

for kk in range(TRIALS):
    i = choice(r)
    j = choice(r)
    match = commonLetter(i,j)
    if match:
        yep += 1
    else:
        nope += 1
    # *** uncomment next line if you want a running score and list of words compared
    # print i,j, yep, nope, (100.*yep)/(yep+nope)

print (100. * yep)/TRIALS
