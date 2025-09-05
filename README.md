# Simple Python IDS

A lightweight network-based Intrusion Detection System (IDS) built in Python using Scapy. This tool monitors live network traffic for common attack patterns (port scans, SYN floods, ICMP floods), logs alerts, and can be extended for real-world deployments.

---t

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Testing](#testing)
10. [Project Structure](#project-structure)

---

## Overview
This project provides a simple, modular IDS that:
- **Sniffs** live packets on a specified interface.
- **Detects** port scans, SYN floods, and ICMP floods using configurable thresholds.
- **Logs** real-time alerts to both console and a persistent log file (`ids.log`).
- **Supports** easy customization and extension for production or home lab environments.

[Back to Top](#table-of-contents)

## Features
- **Real-time packet capture** via Scapy.
- **Signature-free detection** using sliding time windows.
- **Configurable thresholds** in `config.py`.
- **Modular code**: clear separation of logging, detection logic, and entry point.

[Back to Top](#table-of-contents)

## Requirements

### General Requirements
- **Python 3.6+**
- **pip** for installing Python packages.


## Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/yourusername/simple-python-ids.git
cd simple-python-ids
```
2️⃣ (Optional) Create and activate a virtual environment:
Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows (PowerShell)
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```
3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

All detection thresholds are defined in `config.py`. You can edit these values to fine-tune how sensitive the IDS is:

```python
# Port scan detection
PORT_SCAN_PORT_THRESHOLD = 10    # distinct ports within time window
PORT_SCAN_TIME_WINDOW   = 5.0    # seconds

# SYN flood detection
SYN_FLOOD_THRESHOLD     = 20     # SYN packets within time window
FLOOD_TIME_WINDOW       = 5.0    # seconds

# ICMP flood detection
ICMP_FLOOD_THRESHOLD    = 30     # ICMP packets within time window

# Network interface (None = default/first interface)
INTERFACE = None
```

## Usage

The IDS can be run in two modes:

### 🔹 Simulation Mode (safe, no admin privileges required)
Generates fake SYN flood and port scan packets for quick testing:
```bash
cd SIMPLE-IDS
python3 test.py
```
This generates fake attack traffic and feeds it into the IDS.
You should immediately see alerts in the console and in [ids.log], for example:

```bash
YYYY-MM-DD HH:MM:SS WARNING SYN flood from 192.168.0.50: 25 SYNs in last 5.0s
YYYY-MM-DD HH:MM:SS WARNING Port scan from 192.168.0.50: scanned ports=[0, 1, 2, ...]
```
✅ No admin privileges required
✅ Safe — does not affect your system or network

### 🌐 Live Mode (real network traffic)
- Linux/macOS
```bash
sudo python3 main.py
```
- Windows (Admin PowerShell/CMD)
```bash
python main.py
```
Alerts will be written to the console and ids.log when suspicious traffic is detected.
For example, if a port scan or flood is happening on your network, you’ll see warnings logged automatically.

⚠️ Notes:
Requires root/Admin privileges for raw packet capture.
May trigger on normal network activity (false positives).
Use only on networks you own or have permission to monitor.



