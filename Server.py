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

# Function to retrieve news data from the NewsAPI
def retrieveNews (endpoint, params):
    # Add the API key to the parameters
    params['apiKey'] = The_ApiKey
    # Send a GET request to the NewsAPI
    response = requests.get(TheURL + endpoint, params=params)
    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON data
        return response.json()
    else:
        # Return an error message
        return {'status': 'error', 'message': 'Unable to fetch data'}

