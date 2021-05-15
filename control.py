import socket
def control(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '0.0.0.0'
    port = 5455

    sock.connect((host, port))

    #data = sock.recv(2048)

    #data = str(data, "utf-8")

    sock.send(bytes(msg,'utf-8'))
    #print(data)

    sock.close()
