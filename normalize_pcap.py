#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/18 17:35
# @Author : 刘秉星
# @Site : 
# @File : normalize_pcap.py
# @Software: PyCharm
import os
from scapy.all import *


def normalize_pcap(input_folder, output_folder, target_size=784):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if not file_name.endswith(".pcap"):
            continue

        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, file_name)

        with open(input_file, "rb") as f:
            content = f.read(target_size)

        with open(output_file, "wb") as f:
            f.write(content.ljust(target_size, b'\x00'))

        print(f"Normalized {input_file} to {output_file}")


if __name__ == "__main__":
    input_folder = "./output"
    output_folder = "./length_output"
    normalize_pcap(input_folder, output_folder)