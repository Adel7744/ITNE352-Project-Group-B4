import socket
import json

# Constants for server connection
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5555  # The port used by the server

def displayMain():
    # Display the main menu options to the user
    print("\nMain menu:")
    print("1. Search headlines")
    print("2. List of sources")
    print("3. Quit")

def listHeadlinesNews():
    # Display the menu options for searching headlines
    print("\nSearch headlines menu:")
    print("1. Search for keywords")
    print("2. Search by category")
    print("3. Search by country")
    print("4. List all new headlines")
    print("5. Back to the main menu")

def displaySourcesList():
    # Display the menu options for listing news sources
    print("\nList of sources menu:")
    print("1. Search by category")
    print("2. Search by country")
    print("3. Search by language")
    print("4. List all")
    print("5. Back to the main menu")

    def send_request(cs, request):
    # Send a request to the server and handle the response
        cs.send(request.encode('utf-8'))  # Send the request to the server
        response_length_str = cs.recv(1024).decode('utf-8')  # Receive the length of the response
        response_length = int(response_length_str)
        print(f"Received Response length string: {response_length}")
        response_data = b""
    
    # Receive the full response data based on the specified length
        while len(response_data) < response_length:
            part = cs.recv(response_length - len(response_data))
            response_data += part
    
    # Decode the response data from JSON
        return json.loads(response_data.decode('utf-8'))
    
def printResults(news_data):
    # Print the news articles retrieved from the server
    if news_data['status'] == 'ok':
            for i, article in enumerate(news_data['articles']):
                print(f"{i + 1}. {article['title']}")
        
            choice = int(input("Select an article number for details: "))
        
        # Display details of the selected article
            if 1 <= choice <= len(news_data['articles']):
                    article = news_data['articles'][choice - 1]
                    print(f"Title: {article['title']}")
                    print(f"Description: {article['description']}")
                    print(f"Source: {article['source']['name']}")
                    print(f"URL: {article['url']}")
    else:
        print('Failed to fetch news.')

def printSources(sources_data):
    # Print the news sources retrieved from the server
    if sources_data['status'] == 'ok':
        for i, source in enumerate(sources_data['sources']):
            print(f"{i + 1}. {source['name']} ({source['country']})")
    else:
        print('Failed to fetch sources.')