import random
import sys
import socket

def usage():
    usg_str = "Usage: python3 {} $host:$port $dst_file <$input_file\n"
    sys.stderr.write(usg_str.format(sys.argv[0]))
    exit(1)

try:
    host = sys.argv[1].split(':')[0]
    port = int(sys.argv[1].split(':')[1])
    dst_file = sys.argv[2]
except IndexError:
    usage()

def get_chunk(chunk_size=1024, stream=sys.stdin):
    while True:
        data = stream.read(chunk_size) 
        if not data:
            break
        yield data

def client(host, port, dst_file):
    # Pseudo Code:
    #   generate random number as session termination string (see note below)
    r = str(random.randint(1000,5000))
    #   create a udp (socket.SOCK_DGRAM) socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
    #   connect socket to host at port
        sock.connect((host,port))
    except socket.gaierror:
    #   handle case where host does not exist
        print ("invalid host")
    #   send termination string
    sock.send(r.encode())
    #   send dst_file name to server
    sock.send(dst_file.encode())

    for data in get_chunk():
        sock.send(data.encode())
        pass

    sock.send(r.encode())

    sock.close()

if __name__ == "__main__":
    client(host, port, dst_file)
