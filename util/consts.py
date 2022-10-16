"""
this file stores all needed constants
"""
ETHER_TYPE_START = 24
ETHER_TYPE_END = 28
IP_SRC_START = 52
IP_SRC_END = 60
IP_DST_START = 60
IP_DST_END = 68
ARP_START = 40
ARP_END = 44
ARP_SRC_START = 56
ARP_SRC_END = 64
ARP_DST_START = 76
ARP_DST_END = 84
SRC_START = 12
SRC_END = 24
DST_END = 12
ETHERNET_START = 24
ETHERNET_END = 28
IEEE_START = 28
IEEE_END = 32
PID_START = 40
PID_END = 44
SAP_START = 30
SAP_END = 32
IPV4_PROTOCOL_START = 46
IPV4_PROTOCOL_END = 48
SRC_PORT_START = 68
SRC_PORT_END = 72
DST_PORT_START = 72
DST_PORT_END = 76
ICMP_TYPE_START = 68
ICMP_TYPE_END = 70
ICMP_ID_START = 36
ICMP_ID_END = 40
ICMP_FLAGS_START = 40
ICMP_FLAGS_END = 44
TFTP_LEN_START = 76
TFTP_LEN_END = 80
TCP_FLAGS_START = 92
TCP_FLAGS_END = 96
ICMP_PACKET_ID_START = 76
ICMP_PACKET_ID_END = 80
CORRECT_PROTOCOLS = ["TFTP", "ICMP", "ARP", "HTTP", "HTTPS", "TELNET", "SSH", "FTP-DATA", "FTP-CONTROL"]
