import socket

def main():
    ClientSocket = socket.socket()
    host = '127.0.0.1'
    port = 2022

    print("Waiting for connection")
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    while True:
        data = ClientSocket.recv(2048)
        response = "Server message: " + data.decode("utf-8")
        if not data:
            continue
        elif data.decode('utf-8') == "You cannot connect":
            ClientSocket.close()
            break
        Input = input("Write: ")
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    ClientSocket.close()

if __name__ == "__main__":
    main()