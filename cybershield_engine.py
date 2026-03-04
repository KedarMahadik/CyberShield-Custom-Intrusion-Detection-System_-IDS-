from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
import logging
import subprocess
import time
from collections import defaultdict

# 1. Advanced Logging Configuration 
logging.basicConfig(
    filename='ids_security_events.log', 
    level=logging.INFO, 
    format='%(asctime)s | %(levelname)s | %(message)s'
)

# Global Trackers for Behavioral Analysis 
ip_pps_tracker = defaultdict(list) # Packets Per Second
port_scan_tracker = defaultdict(set) # Unique ports per IP
blocked_ips = set()

def block_ip(ip_address):
    """Automated Firewall Management """
    if ip_address not in blocked_ips:
        try:
            # Cross-platform approach (Windows example) 
            command = f"netsh advfirewall firewall add rule name='CyberShield_Block_{ip_address}' dir=in action=block remoteip={ip_address}"
            subprocess.run(command, shell=True, check=True)
            blocked_ips.add(ip_address)
            logging.critical(f"BLOCK_ACTION | IP: {ip_address} | Reason: Threshold Exceeded")
        except Exception as e:
            logging.error(f"SYSTEM_ERROR | Failed to block {ip_address}: {e}")

def analyze_packet(packet):
    """OSI 7-Layer Deep Packet Inspection """
    if not packet.haslayer(IP):
        return

    src_ip = packet[IP].src
    packet_len = len(packet)
    now = time.time()

    # --- LAYER 3/4: DDoS & Rate Limiting  ---
    ip_pps_tracker[src_ip] = [t for t in ip_pps_tracker[src_ip] if now - t < 1]
    ip_pps_tracker[src_ip].append(now)
    
    if len(ip_pps_tracker[src_ip]) > 300: # Threshold: 300 PPS
        logging.warning(f"DDOS_DETECTED | Source: {src_ip} | Rate: {len(ip_pps_tracker[src_ip])} pps")
        block_ip(src_ip)

    # --- LAYER 4: Port Scan Detection  ---
    if packet.haslayer(TCP):
        dst_port = packet[TCP].dport
        port_scan_tracker[src_ip].add(dst_port)
        
        if len(port_scan_tracker[src_ip]) > 20: # Over 20 unique ports
            logging.warning(f"PORT_SCAN | Source: {src_ip} | Unique Ports: {len(port_scan_tracker[src_ip])}")
            block_ip(src_ip)

    # --- LAYER 7: Payload Keyword Inspection (DPI)  ---
    if packet.haslayer(Raw):
        payload = str(packet[Raw].load).upper()
        # Detecting SQL Injection or suspicious command strings 
        sql_keywords = ["SELECT", "UNION", "DROP TABLE", "OR 1=1"]
        if any(key in payload for key in sql_keywords):
            logging.warning(f"SQL_INJECTION_ATTEMPT | Source: {src_ip} | Payload: {payload[:50]}")

def start_ids():
    print("CyberShield Engine Started. Monitoring Traffic...")
    sniff(prn=analyze_packet, store=0)

if __name__ == "__main__":
    start_ids()