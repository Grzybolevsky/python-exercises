#!/usr/bin/env python3
"""Server"""
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s połączył się." % client_address)
        client.send(bytes("Podaj swoje imię", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    name = client.recv(BUFFER_SIZE).decode("utf8")
    welcome = 'Cześć %s!' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s dołączył do czatu!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFFER_SIZE)
        if msg != bytes("{exit}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            print("%s rozłączył się się." % name)
            client.close()
            del clients[client]
            broadcast(bytes("%s opuścił czat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


if __name__ == "__main__":
    clients = {}
    addresses = {}

    HOST = '0.0.0.0'
    PORT = 33000
    BUFFER_SIZE = 1024
    ADDR = (HOST, PORT)

    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)
    SERVER.listen(5)
    print("Oczekiwanie na połączenie...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
