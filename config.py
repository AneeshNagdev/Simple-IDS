# config.py

# --- Port scan detection ---
PORT_SCAN_PORT_THRESHOLD = 10    # distinct ports within time window
PORT_SCAN_TIME_WINDOW   = 5.0    # seconds

# --- SYN flood detection ---
SYN_FLOOD_THRESHOLD     = 20    # SYN packets within time window
FLOOD_TIME_WINDOW       = 5.0   # seconds

# --- ICMP flood detection ---
ICMP_FLOOD_THRESHOLD    = 30    # ICMP packets within time window

# --- Network interface (None = default / first) ---
INTERFACE = None
