from pythonosc import udp_client

HOST = '127.0.0.1'
PORT = 9000 # VRC uses prot 9000 for receiving OSC data.

client = udp_client.SimpleUDPClient(HOST, PORT)
# client.send_message('target', 'data')


client.send_message('/avatar/parameters/Seated', True)