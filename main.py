# main.py

from scapy.all import sniff
import logger_setup, detector, config

def main():
    log = logger_setup.setup_logger()
    ids = detector.IDSDetector(log)

    log.info("=== Simple Python IDS Starting ===")
    sniff(
        iface=config.INTERFACE,
        prn=ids.process_packet,
        store=False
    )

if __name__ == "__main__":
    main()
