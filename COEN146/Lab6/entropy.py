import math
import string
import sys
import fileinput

def entropyCalc():
    entropy = 0
    stream=sys.stdin.read()
    strlng=len(stream)
    for x in range(0,255):
        px=(stream.count(chr(x))/strlng)
        if px > 0:
            entropy += - px*math.log(px, 2)
    return entropy

print(entropyCalc())
