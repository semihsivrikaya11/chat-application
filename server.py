import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"[SERVER] Listening on {HOST}:{PORT}...")

clients = []

def broadcast(message, sender_client=None):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                if client in clients:
                    clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, sender_client=client)
        except:
            break
    if client in clients:
        clients.remove(client)
    client.close()
    print("[DISCONNECT] A client disconnected.")

def receive():
    while True:
        try:
            client, address = server.accept()
            print(f"[CONNECTION] {address} connected.")
            clients.append(client)
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()
        except KeyboardInterrupt:
            print("\n[SHUTDOWN] Server shutting down...")
            server.close()
            break

if __name__ == "__main__":
    receive()
