import socket
import pygame
test1 = 2


sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'
port = 5455

sock.bind((host, port))

while True:
    sock.listen(1)

    conn, addr = sock.accept()

    print(f"Connection with {addr} established.")

    data = conn.recv(1048)

    data = data.decode('utf-8')
    
    if 'play' in data:
        data = data.split(' ')
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(data[1])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            conn, addr = sock.accept()
            data = conn.recv(1048)
            data = data.decode('utf-8')
            print(data)
            if data=='pause':
                pygame.mixer.music.pause()
            if data=='unpause' or 'play' in data:
                pygame.mixer.music.unpause()
            if data=='stop':
                pygame.mixer.music.stop()
    print(data)

sock.close()