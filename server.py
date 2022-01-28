import socket
import os
from _thread import *

status = True


def main():
    players = []
    ServerSideSocket = socket.socket()
    host = '127.0.0.1'
    print(host)
    port = 2022
    ThreadCount = 0

    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print("Socket is listening")
    ServerSideSocket.listen(5)

    while True:
        while ThreadCount <= 3 or status is True:
            Client, address = ServerSideSocket.accept()
            print("Connected to: " + address[0] + ":" + str(address[1]))
            if len(players) == 0:
                start_new_thread(multi_threaded_client1, (Client,))
                ThreadCount += 1
                print("Thread Number: " + str(ThreadCount))
                players.append(address[1])
            elif len(players) < 4:
                start_new_thread(multi_threaded_client, (Client,))
                ThreadCount += 1
                print("Thread Number: " + str(ThreadCount))
                players.append(address[1])
            else:
                Client.send(str.encode("You cannot connect"))
                print("Max number of client is 4.")

    ServerSideSocket.close()


def multi_threaded_client1(connection):
    while True:
        leader = "You are leader of game"
        connection.sendall(str.encode(leader))
        data = connection.recv(2048)
        response = "Server message: " + data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()


def multi_threaded_client(connection):
    while True:
        normal_player_message = "You are normal player"
        connection.sendall(str.encode(normal_player_message))
        data = connection.recv(2048)
        response = "Server message: " + data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()


if __name__ == "__main__":
    main()
