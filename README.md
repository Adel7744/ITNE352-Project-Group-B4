# ITNE352-Project-Group-B4

# Project Description
This project involves a client-server system that retrieves news headlines and sources through the News API. It allows users to engage with the server to search for headlines by keyword, category, or country, and to view all headlines. Additionally, users have the ability to search for news sources by category, country, or language, or to display a list of all sources.

# Group
Group No. : B4

Course code: ITNE352/ITCE320

Section No. : 02

Students Names: ADEL JEDAAN , YOUSIF ALSHUROOQI

Students IDs: 202201372 , 202100506 
Semester  2023/2024

# Table of Contents
Requirements
How to Run
The Scripts
Additional Concepts
Acknowledgments
Conclusion


# Requirements:

1. Install Python: Ensure that you have Python 3.x installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/.

2. Install Required Dependencies: The project uses the following Python libraries:
socket: Provides access to the BSD socket interface.

3. threading: Allows the creation and management of separate threads of execution.

4. tkinter : Allow you to design GUI

5. json : Handle json data 

6. Set up the Development Environment: Ensure that you have a text editor or an IDE of your choice installed on your system such as Visual Studio Code

7. Api key from newsapi.org


# How to run: 

To run the Collaborative Server-Client Application, follow these steps:

1. Run the server.py script in your terminal or command prompt. 
2. Run the GUIclient.py to show the output as graphical user interface or run client.py to show as output only script in separate terminal or command prompt windows to simulate multiple clients connecting to the server. Each client will be able to interact with the server and other connected clients.
3. Interact with the Application: Once the clients are connected, you can start collaborating by sending messages, sharing files, and synchronizing data between the clients through the server.

# Server Script
File: "Server.py"

 Main Functionalities:

1. Sets up a TCP server to accept and process incoming client connections.
2. Employs threading to manage and service multiple client connections concurrently.
3. Fetches news data from the NewsAPI.org service based on specific client requests.
4. Transmits the requested news data back to clients in response to their inquiries.


 Packages Used:
 
1. socket - To create network connections for the TCP server.
2. json - To handle JSON data for communication with the NewsAPI.org service and the clients.
3. threading -To enable the server to handle multiple client connections concurrently.
4. requests - To make HTTP requests to the NewsAPI.org service and fetch the news data.


# Client Script
File: "GuiClient.py" if you want with graphical user interface or "Client.py" to use it as command line

 Main Functionalities:
1. Establishes a TCP connection with the news server .
2. Presents a main menu with options to view the latest news headlines and available news sources.
3. Includes a search functionality for news based on keywords, categories, or countries.
4. Displays detailed information about selected news articles, such as the title, description, and URL.
5. Uses a GUI to handle all user inputs, display news details, and send requests to the server.

Packages Used:
1. socket 
2. json 
3. import tkinter as tk - This line imports the Tkinter library, which is a standard Python GUI (Graphical User Interface) toolkit.
4. from tkinter import messagebox, simpledialog - This line imports two specific modules from the Tkinter library - messagebox and simpledialog - which provide functions for displaying message boxes and simple dialog boxes, respectively.


# Acknowledgments
The project was developed as part of the ITNE352 course at the University Of Bahrain. We would like to thank the course instructor, 
Dr.Mohamed Almeer, for their guidance and support throughout the whole semester.

# Conclusion
In conclusion, developing the Server-Client Application was a time-consuming journey, but it was worth it. We extended our gratitude to Dr.Mohamed Almeer for his guidance and support throughout the project. This experience not only enhanced our understanding of networking concepts but also sharpened our skills in implementing complex systems. Additionally, integrating the graphical user interface (GUI) added a user-friendly touch to the application, making it more accessible to users. Overall, we are thankful for the opportunity to undertake this project and for the invaluable lessons learned along the way.
