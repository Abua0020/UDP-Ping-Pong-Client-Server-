# UDP-Ping-Pong-Client-Server-
By: Abdulrahman Abu Alhussein 
====================================

Overview:
-----------
This program uses a basic UDP-based ping-pong communication system between a client and a server

- The Client sends 10 ping messages to the Server
- The Server responds with pong messages while having random delays and packet drops
- The Client calculates the Round Trip Time (RTT) for each message and reports the statistics at the end

Files:
------
1. server.py - The server-side script that listens for pings and sends pongs
2. client.py - The client-side script that sends pings and measures RTT for each pong received

How to Run:
-----------
1. First, start the server:
The server will listen on port 12000 for incoming ping messages

2. Then, start the client:
The client will send 10 ping messages to the server and receive pong responses

3. After the client completes 10 pings, it will ask you:
- Type 'yes' to run another session
- Type 'no' to exit

Requirements:
-------------
- Python

Disclaimer:
------------
- I added the option to either end the program or try another session because I was running into
  some issues with socket reuse and connection issues. This helped reset the client-server communication
  and makes sure that the sockets are properly closed and reopened for each session, which 
  improves the reliability of the connection.
