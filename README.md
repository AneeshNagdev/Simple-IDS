# Simple Python IDS

A lightweight network-based Intrusion Detection System (IDS) built in Python using Scapy. This tool monitors live network traffic for common attack patterns (port scans, SYN floods, ICMP floods), logs alerts, and can be extended for real-world deployments.

---t

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
   - [General Requirements](#general-requirements)
   - [Windows Requirements](#windows-requirements)
   - [Linux/macOS Requirements](#linuxmacos-requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Testing](#testing)
8. [Environment Notes](#environment-notes)
9. [Extending](#extending)
10. [Project Structure & /venv](#project-structure--venv)

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
- **Virtual environment** (recommended): isolates dependencies in `/venv`.
- **pip** for installing Python packages.

Install dependencies:
```bash
pip install -r requirements.txt

Windows Requirements

1. Download and install Npcap
 (run installer as Administrator).

2. During installation, enable:

   “WinPcap API-compatible Mode”

   “Restrict Npcap driver’s access to Administrators only”

3. Reboot if prompted.

4. Run IDS from an elevated PowerShell or CMD:

```bash
python main.py