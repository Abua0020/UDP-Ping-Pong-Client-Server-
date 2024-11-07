#Assignment 2, NET4005 
# by: Abdulrahman Abu Alhussein 

import socket
import random
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12000))
server_socket.settimeout(5)  # Set a timeout
print("Server ready to receive pings")

while True:
    packets_dropped = 0  # Reset number of dropped for each session
    print("New session started.")

    for i in range(10):  # 10 pings per session
        try:
            message, client_address = server_socket.recvfrom(1024)
            print(f"Ping {i+1} received from {client_address}")  
            
            # Drop packet randomly 
            if packets_dropped < 5 and random.random() < 0.5:  # 50% chance to drop
                print(f"Packet {i+1} dropped")
                packets_dropped += 1
                continue  
            
            # random delay between 100 and 500 ms
            delay = random.uniform(0.1, 0.5)  
            time.sleep(delay)
            
            server_socket.sendto("pong".encode(), client_address)
            print(f"Ping {i+1} responded to with delay of {delay*1000:.2f} ms")
        except socket.timeout:
            print("Server timed out waiting for client ping")

    print("Session complete, waiting for new session.")
