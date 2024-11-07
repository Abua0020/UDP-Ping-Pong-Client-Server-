# by: Abdulrahman Abu Alhussein 101157537

import socket
import time
import random

server_address = ('localhost', 12000)
initial_timeout = 2  
max_timeouts = 5  # Max allowed to drop

def run_client():
    # Create a new socket each time
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    client_socket.settimeout(initial_timeout)  # Sets the initial timeout

    rtts = []
    num_lost = 0
    timeout = initial_timeout  # Start with a new timeout

    for i in range(10):
        if num_lost >= max_timeouts: 
            print(f"Reached maximum timeouts ({max_timeouts}). Stopping further pings.")
            break

        message = f"ping {i+1}"
        start_time = time.time()

        try:
            client_socket.sendto(message.encode(), server_address)
            response, server = client_socket.recvfrom(1024)
            rtt = (time.time() - start_time) * 1000
            rtts.append(rtt)
            print(f"Received: {response.decode()} RTT: {rtt:.2f} ms")
            timeout = initial_timeout  
            client_socket.settimeout(timeout)  # Reset the timeout after success
        except socket.timeout:
            print(f"Request timed out for ping {i+1}")
            num_lost += 1
            timeout = min(timeout * 2, initial_timeout * max_timeouts)  # back off
            client_socket.settimeout(timeout)  

    # last RTT and packet loss calculations
    if rtts:
        min_rtt = min(rtts)
        max_rtt = max(rtts)
        avg_rtt = sum(rtts) / len(rtts)
    else:
        min_rtt = max_rtt = avg_rtt = 0

    packet_loss_rate = (num_lost / 10) * 100

    print(f"Min RTT: {min_rtt:.2f} ms")
    print(f"Max RTT: {max_rtt:.2f} ms")
    print(f"Avg RTT: {avg_rtt:.2f} ms")
    print(f"Packet loss rate: {packet_loss_rate}%")

    client_socket.close()  # Cleans socket

# Runs the client in one session and ask for additional sessions
while True:
    print("\n--- Starting a new session ---\n")
    run_client()

    another = input("Do you want to run another session? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Exiting the client")
        break

    time.sleep(1)  
