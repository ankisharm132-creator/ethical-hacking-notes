import socket

def scan(target):
    ip = socket.gethostbyname(target)
    print("Target: " + target)
    print("IP: " + ip)
    print("---")

scan("google.com")
scan("facebook.com")
scan("youtube.com")
