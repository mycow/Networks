import sys
import socket

def usage():
    usg_str = "Usage: python3 {} $port\n"
    sys.stderr.write(usg_str.format(sys.argv[0]))
    exit(1)

try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    usage()
    
def listen(port, chunk_size=1024):
    #   open udp (socket.SOCK_DGRAM) socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #   bind socket to listen at port 
    sock.bind(('',port))
    while True:
        (line,address) = sock.recvfrom(chunk_size)
        line = line.decode()
        #if quit is received, exit
        if line == "quit":
            break
        print('{}: {}'.format(address[0],line))
    pass

    sock.close()

if __name__ == "__main__":
    listen(port)

