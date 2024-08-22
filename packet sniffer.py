from scapy.all import *

def packet_handler(packet):
    """Handles captured packets."""
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")

        # Extract payload data based on the protocol
        

if __name__ == "__main__":
    sniff(prn=packet_handler, filter="ip")