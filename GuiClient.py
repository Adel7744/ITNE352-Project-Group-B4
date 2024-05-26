import socket  
import json  
import tkinter as tk  # Import tkinter module for GUI
from tkinter import messagebox, simpledialog  # Import specific tkinter functions

# Constants for server connection
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5555  # The port used by the server

def send_request(cs, request):
    # Send a request to the server and handle the response
    cs.send(request.encode('utf-8'))  # Send the request to the server
    response_length_str = cs.recv(1024).decode('utf-8')  # Receive the length of the response
    response_length = int(response_length_str)  # Convert response length to integer
    print(f"Received Response length string: {response_length}")
    response_data = b""
    
    # Receive the full response data based on the specified length
    while len(response_data) < response_length:
        part = cs.recv(response_length - len(response_data))
        response_data += part
    
    # Decode the response data from JSON
    return json.loads(response_data.decode('utf-8'))

def display_results(news_data):
    # Display news articles in a new window
    if news_data['status'] == 'ok':
        results_window = tk.Toplevel(root)  # Create a new window
        results_window.title("News Results")  # Set the title of the window
        for i, article in enumerate(news_data['articles']):
            tk.Label(results_window, text=f"{i + 1}. {article['title']}").pack()  # Display each article title
        tk.Label(results_window, text="Select an article number for details").pack()  # Prompt for article selection
        article_number = simpledialog.askinteger("Input", "Enter article number:")  # Get the article number from user
        if 1 <= article_number <= len(news_data['articles']):
            article = news_data['articles'][article_number - 1]
            messagebox.showinfo("Article Details", f"Title: {article['title']}\nDescription: {article['description']}\nSource: {article['source']['name']}\nURL: {article['url']}")
    else:
        messagebox.showerror("Error", "Failed to fetch news.")  # Show error if news fetch fails

def display_sources(sources_data):
    # Display news sources in a new window
    if sources_data['status'] == 'ok':
        sources_window = tk.Toplevel(root)  # Create a new window
        sources_window.title("News Sources")  # Set the title of the window
        for i, source in enumerate(sources_data['sources']):
            tk.Label(sources_window, text=f"{i + 1}. {source['name']} ({source['country']})").pack()  # Display each source
    else:
        messagebox.showerror("Error", "Failed to fetch sources.")  # Show error if sources fetch fails

def search_headlines(cs):
    option = simpledialog.askinteger("Input", "Search headlines menu:\n1. Search for keywords\n2. Search by category\n3. Search by country\n4. List all new headlines\n5. Back to the main menu\nSelect an option:")  # Get user choice
    if option == 1:
        keyword = simpledialog.askstring("Input", "Enter keyword:")  # Get keyword from user
        params = {'q': keyword}
        news_data = send_request(cs, f'1.everything.{json.dumps(params)}')  # Send request with keyword
        display_results(news_data)
    elif option == 2:
        category = simpledialog.askstring("Input", "Enter category (e.g., business, entertainment, general, health, science, sports, technology):")  # Get category from user
        params = {'category': category}
        news_data = send_request(cs, f'1.top-headlines.{json.dumps(params)}')  # Send request with category
        display_results(news_data)
    elif option == 3:
        country = simpledialog.askstring("Input", "Enter country code (au, nz, ca, ae, sa, gb, us, eg, ma, etc.):")  # Get country code from user
        params = {'country': country}
        news_data = send_request(cs, f'1.top-headlines.{json.dumps(params)}')  # Send request with country code
        display_results(news_data)
    elif option == 4:
        news_data = send_request(cs, '1.top-headlines.{}')  # Send request to list all headlines
        display_results(news_data)
    elif option == 5:
        return  # Return to main menu
    else:
        messagebox.showerror("Error", "Invalid input. Please enter again...")  # Show error for invalid input

def list_sources(cs):
    option = simpledialog.askinteger("Input", "List of sources menu:\n1. Search by category\n2. Search by country\n3. Search by language\n4. List all\n5. Back to the main menu\nSelect an option:")  # Get user choice
    if option == 1:
        category = simpledialog.askstring("Input", "Enter category (e.g., business, entertainment, general, health, science, sports, technology):")  # Get category from user
        params = {'category': category}
        sources_data = send_request(cs, f'2.sources.{json.dumps(params)}')  # Send request with category
        display_sources(sources_data)
    elif option == 2:
        country = simpledialog.askstring("Input", "Enter country code (e.g., au, nz, ca, ae, sa, gb, us, eg, ma):")  # Get country code from user
        params = {'country': country}
        sources_data = send_request(cs, f'2.sources.{json.dumps(params)}')  # Send request with country code
        display_sources(sources_data)
    elif option == 3:
        language = simpledialog.askstring("Input", "Enter language code (en, fr, de, es, ar, etc.):")  # Get language code from user
        params = {'language': language}
        sources_data = send_request(cs, f'2.sources.{json.dumps(params)}')  # Send request with language code
        display_sources(sources_data)
    elif option == 4:
        sources_data = send_request(cs, '2.sources.{}')  # Send request to list all sources
        display_sources(sources_data)
    elif option == 5:
        return  # Return to main menu
    else:
        messagebox.showerror("Error", "Invalid input. Please enter again")  # Show error for invalid input

def start_client():
    # Create a socket and connect to the server
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((HOST, PORT))  # Connect to the server
    print("Connected to server.")
    
    client_name = simpledialog.askstring("Input", "Enter your name:")  # Get client's name
    cs.send(client_name.encode('utf-8'))  # Send the client's name to the server
    
    def on_search_headlines():
        search_headlines(cs)  # Call function to search headlines
    
    def on_list_sources():
        list_sources(cs)  # Call function to list sources
    
    def on_quit():
        cs.close()  # Close the socket
        root.quit()  # Quit the application

    # Create the main window
    global root
    root = tk.Tk()
    root.title("News Client")  # Set the title of the window
    
    # Create buttons for the main menu
    tk.Button(root, text="Search Headlines", command=on_search_headlines).pack(pady=10)  # Button to search headlines
    tk.Button(root, text="List Sources", command=on_list_sources).pack(pady=10)  # Button to list sources
    tk.Button(root, text="Quit", command=on_quit).pack(pady=10)  # Button to quit the application
    
    root.mainloop()  # Start the main event loop

if __name__ == '__main__':
    start_client()  # Start the client
