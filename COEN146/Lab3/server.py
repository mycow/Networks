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
    
def server(port, chunk_size=1024):
    # Pseudo Code:
    #   open udp (socket.SOCK_DGRAM) socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #   bind socket to listen at port 
    sock.bind(('',port))
    #   receive session termination string from client (see note below)
    r = sock.recv(chunk_size).decode()
    #   receive dst_file name from client
    dst_file = sock.recv(chunk_size).decode()
    #   open dst_file for writing
    f = open(dst_file, "w")
    while True:
        data = sock.recv(chunk_size).decode()
        if data == r:
            break
        f.write(data)
    pass

    sock.close()

if __name__ == "__main__":
    server(port)

