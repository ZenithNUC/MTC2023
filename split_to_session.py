from scapy.all import *
from collections import defaultdict
import os


def parse_pcap(file_name):
    sessions = defaultdict(list)
    packets = rdpcap(file_name)

    for packet in packets:
        if 'IP' in packet and ('TCP' in packet or 'UDP' in packet):
            proto = 'TCP' if 'TCP' in packet else 'UDP'
            flow_key = tuple(sorted([f"{packet['IP'].src}:{packet[proto].sport}",
                                     f"{packet['IP'].dst}:{packet[proto].dport}"]))

            # Set IP and port fields to default values
            packet['IP'].src = "0.0.0.0"
            packet['IP'].dst = "0.0.0.0"
            packet[proto].sport = 0
            packet[proto].dport = 0

            sessions[flow_key].append(packet)

    return sessions


def create_output_files(sessions, output_prefix):
    output_dir = os.path.dirname(output_prefix)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, (flow_key, packets) in enumerate(sessions.items()):
        output_file = f"{output_prefix}_{i}.pcap"
        wrpcap(output_file, packets)
        print(f"Created {output_file} with {len(packets)} packets")


if __name__ == "__main__":
    input_file = "Tinba.pcap"
    output_prefix = "output/session"

    sessions = parse_pcap(input_file)
    create_output_files(sessions, output_prefix)