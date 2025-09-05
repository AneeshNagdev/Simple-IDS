# detector.py

import time
from scapy.all import TCP, ICMP, IP
from collections import defaultdict, deque
import logging
import config

class IDSDetector:
    def __init__(self, logger: logging.Logger):
        self.log = logger

        # Use deque for efficient pops from left
        self.syn_times = defaultdict(deque)      
        self.icmp_times = defaultdict(deque)    

        # For port scans: track ports + timestamps
        self.scan_ports = defaultdict(lambda: {"ports": set(), "times": deque()})

    def _purge_old(self, dq: deque, window: float):
        """Remove timestamps older than window from left."""
        now = time.time()
        while dq and now - dq[0] > window:
            dq.popleft()

    def process_packet(self, pkt):
        now = time.time()

        # --- TCP SYN detection ---
        if pkt.haslayer(TCP) and pkt[TCP].flags & 0x02:
            src = pkt[IP].src
            dst_port = pkt[TCP].dport

            # SYN flood
            syn_q = self.syn_times[src]
            syn_q.append(now)
            self._purge_old(syn_q, config.FLOOD_TIME_WINDOW)
            if len(syn_q) > config.SYN_FLOOD_THRESHOLD:
                self.log.warning(
                    f"SYN flood from {src}: {len(syn_q)} SYNs in last {config.FLOOD_TIME_WINDOW}s"
                )

            # Port scan
            rec = self.scan_ports[src]
            rec["ports"].add(dst_port)
            rec["times"].append(now)
            self._purge_old(rec["times"], config.PORT_SCAN_TIME_WINDOW)
            # Rebuild ports set to only include those in window
            rec["ports"] = {p for p, t in zip(rec["ports"], rec["times"]) 
                            if now - t <= config.PORT_SCAN_TIME_WINDOW}
            if len(rec["ports"]) > config.PORT_SCAN_PORT_THRESHOLD:
                self.log.warning(
                    f"Port scan from {src}: scanned ports={sorted(rec['ports'])}"
                )

        # --- ICMP flood detection ---
        elif pkt.haslayer(ICMP):
            src = pkt[IP].src
            icmp_q = self.icmp_times[src]
            icmp_q.append(now)
            self._purge_old(icmp_q, config.FLOOD_TIME_WINDOW)
            if len(icmp_q) > config.ICMP_FLOOD_THRESHOLD:
                self.log.warning(
                    f"ICMP flood from {src}: {len(icmp_q)} ICMPs in last {config.FLOOD_TIME_WINDOW}s"
                )
