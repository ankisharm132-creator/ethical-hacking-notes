import socket

file = open("scan_results.txt", "w")
file.write("=== Scan Results ===\n")

websites = ["google.com", "facebook.com", "youtube.com"]

for site in websites:
    ip = socket.gethostbyname(site)
    result = site + " = " + ip + "\n"
    print(result)
    file.write(result)

file.close()
print("Results saved!")
