import json
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

def compute_checksum(data, bound=256):
    return sum(data.encode()) % bound




def reliable_recv(udp_socket, packet_size=1024):
    # initialize/create acknowledgement packet
    ack = dict()
    while True:
    #   receive packet from client
        (packet, address) = udp_socket.recvfrom(packet_size)
        packet = json.loads(packet.decode())
    #   deserialize packet
    #   compute checksum of data in packet
        cs = compute_checksum(packet["data"])
    #   compare computed checksum with checksum in packet
    #   if they match:
        if packet["checksum"] == cs:
            ack["sequence"] = packet["sequence"] + 1
            udp_socket.sendto((json.dumps(ack).encode()), address)
            break
        else:
            ack["sequence"] = packet["sequence"]
            udp_socket.sendto((json.dumps(ack).encode()), address)
            continue
    #     set acknowledgement packet sequence to packet's sequence + 1
    #     send acknowledgement packet to client
    #   else:
    #     set acknowledgement packet sequence to packet's sequence
    #     send acknowledgement packet to client
    #     repeat loop
    # return packet's data
    return packet["data"]
    pass




def server(port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind( ("", port) )
    term_string = reliable_recv(udp_socket)
    dst_file = reliable_recv(udp_socket)

    with open(dst_file, "w") as stream:
        while True:
            data = reliable_recv(udp_socket)
            if data == term_string:
                break
            stream.write(data)
    udp_socket.close()




if __name__ == "__main__":
    server(port)
