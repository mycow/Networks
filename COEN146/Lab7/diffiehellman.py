import sys

# do not modify this function
def get_input():
    # default prime and base
    prime = 64303
    base = 6

    # attempt to get input
    try:
      a_pk = int(sys.argv[1])
      b_pk = int(sys.argv[2])
      if len(sys.argv) > 3:
        prime = int(sys.argv[3])
        base = int(sys.argv[4])
    except (IndexError, ValueError):
      fmt_str = "Usage:\n" \
                "\tpython3 {} <a_pk> <b_pk> [<prime> <base>]\n"
      sys.stderr.write(fmt_str.format(sys.argv[0]))
      sys.exit(1)

    # return input
    return a_pk, b_pk, prime, base

if __name__ == "__main__":
    a_pk, b_pk, prime, base = get_input()
    # do your computation here
    k = (base**(a_pk**b_pk))%prime
    print("Shared Key: ", k)
