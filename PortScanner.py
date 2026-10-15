import socket
from IPy import IP

def scan(target):
    converted_ip = checkIP(target)
    print('\n' + ' [_0 Scanning Target] ' + str(target))
    for port in range(1,30000):
        scan_port(converted_ip,port)

def checkIP(ip):
        try:
            IP(ip)
            return(ip)
        except ValueError:
            return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[#] Open Port ' + str(port) + ' :  ' + str(banner.decode().strip('\n')))
        except:
            print(' [#] Open Port ' + str(port))
    except:
        pass
       # print('[#] Port ' + str(port) + ' Is Closed')


targets = input('[#] Enter Target Target/s to Scan (split Multiple Target with ,) : ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(''))
else:
    scan(targets)
