SERVER_IP = '10.0.0.101' # My LAN IP
PORT = 5505
SERVER_ADDRESS = (SERVER_IP, PORT)
BUFFER_SIZE = 2048
MAX_CONNECTIONS = 5
REQUEST = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % TARGET_HOST
OK_MESSAGE = "HTTP/1.1 200 OK\r\n"