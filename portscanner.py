import socket

def scan_port(host, port):
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
        print("Port " + str(port) + " OPEN!")
    s.close()

print("Scanning google.com...")
for port in range(70, 90):
    scan_port("google.com", port)
print("Done!")
