from scapy.all import IP, TCP
from detector import IDSDetector
import logger_setup

log = logger_setup.setup_logger()
ids = IDSDetector(log)

# --- SYN Flood Test ---
for i in range(25):  # > SYN_FLOOD_THRESHOLD
    pkt = IP(src="192.168.0.50", dst="192.168.0.1") / TCP(dport=80, flags="S")
    ids.process_packet(pkt)

# --- Port Scan Test ---
for port in range(20):  # > PORT_SCAN_PORT_THRESHOLD
    pkt = IP(src="192.168.0.50", dst="192.168.0.1") / TCP(dport=port, flags="S")
    ids.process_packet(pkt)
