import socket
from urllib.parse import urlparse
def ip_converter(dns):
    try:
        hostname = urlparse(dns).hostname
        ip = socket.gethostbyname(hostname)
        return f"Your DNS is {dns} and its IP Address is : {ip}"
    except socket.error as e:
        return f"Error: {e} occurred"

def portScanner():
    user = input("Enter DNS: ")
    host = ip_converter(user)
    if host.startswith("Erorr"):
        return False
    for i in range(1, 1600):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((host.split()[-1], i))
        if result:
            continue
        else:
            print(f"Port {i} is open")
            s.close()
portScanner()
