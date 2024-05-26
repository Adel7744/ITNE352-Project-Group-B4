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

def bringHeadlinesNews(cs):
    # Handle the user input for searching headlines
    listHeadlinesNews()
    option = input("Select an option: ")  # Get the user's option

    # Handle the user's choice
    if option == '1':
        keyword = input("Enter keyword: ")
        params = {'q': keyword}
        news_data = send_request(cs, f'1.everything.{json.dumps(params)}')
        printResults(news_data)
    elif option == '2':
        category = input("Enter category (e.g., business, entertainment, general, health, science, sports, technology): ")
        params = {'category': category}
        news_data = send_request(cs, f'1.top-headlines.{json.dumps(params)}')
        printResults(news_data)
    elif option == '3':
        country = input("Enter country code (au, nz, ca, ae, sa, gb, us, eg, ma, etc.): ")
        params = {'country': country}
        news_data = send_request(cs, f'1.top-headlines.{json.dumps(params)}')
        printResults(news_data)
    elif option == '4':
        news_data = send_request(cs, '1.top-headlines.{}')
        printResults(news_data)
    elif option == '5':
        return
    else:
        print("Invalid input. Please enter again...")

def bringSourceList(cs):
    # Handle the user input for listing sources
    displaySourcesList()
    option = input("Select an option: ")  # Get the user's option

    # Handle the user's choice
    if option == '1':
        category = input("Enter category (e.g., business, entertainment, general, health, science, sports, technology): ")
        params = {'category': category}
        sources_data = send_request(cs, f'2.sources.{json.dumps(params)}')
        printSources(sources_data)
    elif option == '2':
        country = input("Enter country code (e.g., au, nz, ca, ae, sa, gb, us, eg, ma): ")
        params = {'country': country}
        sources_data = send_request(cs, f'2.sources.{json.dumps(params)}')
        printSources(sources_data)
    elif option == '3':
        language = input("Enter language code (en, fr, de, es, ar, etc.): ")
        params = {'language': language}
        sources_data = send_request(cs, f'2.sources.{json.dumps(params)}')
        printSources(sources_data)
    elif option == '4':
        sources_data = send_request(cs, '2.sources.{}')
        printSources(sources_data)
    elif option == '5':
        return
    else:
        print("Invalid input. Please enter again")

def startClient():
    # Create a socket and connect to the server
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((HOST, PORT))
    print("Connected to server.")
    
    client_name = input("Enter your name: ")
    cs.send(client_name.encode('utf-8'))  # Send the client's name to the server
    
    while True:  # Main loop to display the main menu and handle user choices
        displayMain()
        option = input("Select an option: ")  # Handle the user's choice
        
        if option == '1':
            bringHeadlinesNews(cs)
        elif option == '2':
            bringSourceList(cs)
        elif option == '3':
            print("Quitting...")
            break
        else:
            print("Invalid input. Please enter again.")

    # Close the socket connection
    cs.close()

if __name__ == '__main__':
    startClient()