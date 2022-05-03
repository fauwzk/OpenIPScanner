import ipaddress
from pythonping import ping
import socket
import time

addressMin = int(ipaddress.IPv4Address(str(input("address min: "))))
addressMax = int(ipaddress.IPv4Address(str(input("address max: "))))

total_address = addressMax - addressMin
i = 0
ip_list = []
workingip_list = []
workingipping_list = []
notworkingip_list = []

def test_port(ip):
	a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	a_socket.settimeout(0.1)
	location = (ip, 21)
	result_of_check = a_socket.connect_ex(location)
	if result_of_check == 0:
		print("Port is open")
	else:
		print("Port is not open")
	a_socket.close()

def test_ip(ip):
	a = ping(ip, count=1, timeout=0.1)
	if a.success() == True:
		print(f"Work: {ip} Ping: {a.rtt_avg_ms}ms")
		workingip_list.append(ip)
		test_port(ip)
		# workingipping_list.append(a.rtt_avg_ms)
	else:
		#print(f"Not work: {ip}")
		notworkingip_list.append(ip)

while True:
	ip = ip1 + i
	if i > total_address:
		break
	else:
		ip = str(ipaddress.IPv4Address(ip))
		# ip_list.append(ip)
		test_ip(ip)
	i = i + 1

print(f"Working IPs ({len(workingip_list)}/{total_address}): {workingip_list}")