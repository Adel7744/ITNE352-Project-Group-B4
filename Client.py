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