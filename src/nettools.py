from pythonping import ping
import socket
import ipaddress
import sys

def testPorts(ip, ports):
	a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	a_socket.settimeout(0.1)
	for x in ports:
		location = (ip, int(x))
		result_of_check = a_socket.connect_ex(location)
		if result_of_check == 0:
			print(f"Port {x} is open")
		else:
			if showFail == 1:
				print(f"Port {x} is not open")
			continue
		a_socket.close()

def main(addressMin, addressMax, ports, showfail):
	global workingip_list, notworkingip_list
	workingip_list = []
	notworkingip_list = []
	global showFail
	showFail = showfail
	global totalAddress
	totalAddress = int(ipaddress.IPv4Address(str(addressMax))) - int(ipaddress.IPv4Address(str(addressMin)))
	ipEnd = 0
	while ipEnd <= totalAddress:
		ip = str(ipaddress.IPv4Address(int(ipaddress.IPv4Address(addressMin)) + ipEnd))
		ipEnd += 1
		a = ping(ip, count=1, timeout=0.1)
		if a.success() == True:
			print(f"Work: {ip} Ping: {a.rtt_avg_ms}ms")
			workingip_list.append(ip)
			if ports != 0:
				testPorts(ip, ports)
		else:
			if showFail == 1:
				print(f"Not working: {ip}")
			notworkingip_list.append(ip)