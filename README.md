# Chat Application

This project is a simple text-based chat application developed using Python. It allows multiple users to connect to a common server and exchange messages in real time.

## Technologies Used

- Python 3
- Socket programming
- Threading

## Project Overview

The application consists of two main parts:

- **Server:** Listens for incoming connections and broadcasts messages to all connected clients.
- **Client:** Allows users to connect to the server with a nickname and send/receive messages.

Each client connects with a unique nickname. Messages sent by one user are instantly delivered to all other users in the chat.

## How to Run

1. Open a terminal and start the server:
   ```
   python server.py
   ```
2. Open another terminal for the client and run:
   ```
   python client.py
   ```
3. Enter a nickname when prompted.
4. You can open multiple terminals and run additional clients to join the chat.

## Purpose

This project demonstrates the basics of socket programming and how to handle multiple connections using threads. It’s a great introduction to real-time communication systems in Python.

## Note

This application is intended for educational purposes and runs on localhost for testing and demonstration.
