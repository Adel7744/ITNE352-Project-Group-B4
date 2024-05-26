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
    
 # Function to save the retrieved news data to a file
def saveDataToFile (group_id, client_name, option, data):
    # Construct the filename based on the input parameters
    filename = f"{group_id}_{client_name}_{option}.json"
    # Write the data to the file in JSON format
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)   


# Function to handle the client request
def manageUserRequest(client_socket, addr):
    print(f"Start connection {addr}")
    try:
        # Receive the client name
        client_name = client_socket.recv(1024).decode('utf-8')
        print(f"Client Name: {client_name}")
        # Handle the client request
        while True:
            # Receive the request from the client
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break
            print(f"The Client: {client_name}, Request: {request}")
            # Check if the request is for news data
            if request.startswith('1.') or request.startswith('2.'):
                # Split the request into the endpoint and parameters
                _, endpoint, params_json = request.split('.', 2)
                params = json.loads(params_json)
                # Retrieve the news data
                news_data = retrieveNews (endpoint, params)
                # Extract the main option from the endpoint
                option = endpoint.split('.')[0]
                # Save the news data to a file
                saveDataToFile ("B4", client_name, f"{option}", news_data)
                # Send the response to the client
                response = json.dumps(news_data).encode('utf-8')
                response_length = len(response)
                print(f"Sending response length: {response_length}")
                client_socket.sendall(str(response_length).encode('utf-8').ljust(10))
                client_socket.sendall(response)
                print("Response sent")
            else:
                # Send an error response to the client
                error_response = json.dumps({'status': 'error', 'message': 'Invalid request'}).encode('utf-8')
                client_socket.sendall(str(len(error_response)).encode('utf-8').ljust(10))
                client_socket.sendall(error_response)
    except ConnectionResetError:
        pass
    finally:
        # Disconnect the client
        print(f"Client {client_name} disconnected")
        client_socket.close()

# Start the server
if __name__ == '__main__':
    startServer()

