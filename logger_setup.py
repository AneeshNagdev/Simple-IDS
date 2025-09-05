# logger_setup.py

import logging

def setup_logger(logfile: str = "ids.log"):
    """
    Configure root logger to log INFO+ to both console and logfile.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(logfile),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()
