import random
import sys
import math

def random_data(size):
    for i in range(0,size):
        c = chr(random.getrandbits(8))
        r = ord(c)
        sys.stdout.write(c)

    pass

#def perfect_eight():
 # """<Write what this function does here>
  #"""
   # sys.stderr.write("perfect_eight not implemented\n")



# the following code is provided to you for free
if __name__ == "__main__":
    try:
        which = sys.argv[1]
        if which == "random":
            size = int(sys.argv[2])
            random_data(size)
        elif which == "perfect":
            perfect_eight()
        else:
            raise IndexError("invalid option")
    except IndexError as e:
        usage_str = "Usage:\n"                 \
            "\tpython3 {prog} random <size>\n" \
            "\tpython3 {prog} perfect\n"
        sys.stderr.write(usage_str.format(prog=sys.argv[0]))
        sys.exit(1)




