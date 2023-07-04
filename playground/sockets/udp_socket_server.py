import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # dgram is UDP
udp_socket.bind(("127.0.0.1", 5000))

msg, addr = udp_socket.recvfrom(1024)
print('Server UDP msg received: ', msg.upper())

udp_socket.close()



