import socket

input("press enter for connection");
conn = socket.socket()
conn.connect( ("127.0.0.1", 8888) )

while True:
    command = input()
    conn.send(bytes(command, "utf-8"))
    while True:
        try:
            response = conn.recv(1024)
            print(response.decode("utf-8"))
            break
        except Exception:
            pass