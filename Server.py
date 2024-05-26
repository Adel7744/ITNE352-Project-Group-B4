import socket
import json
import threading
import requests

The_ApiKey = 'c7f93d27e641492e9f7ee1f87e5ea186'
TheURL = 'https://newsapi.org/v2/'
HOST = '127.0.0.1'
PORT = 5555

def startServer():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind((HOST, PORT))
    ss.listen(3)
    print(f"The Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = ss.accept()
        client_handler = threading.Thread(target=manageUserRequest, args=(client_socket, addr))
        client_handler.start()


