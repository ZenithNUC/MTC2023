#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/19 22:04
# @Author : 刘秉星
# @Site : 
# @File : traffic_to_png.py
# @Software: PyCharm
import os
import math
import numpy as np
from PIL import Image
from scapy.all import rdpcap


def process(pcap_file, image_file):
    packets = rdpcap(pcap_file)
    data = b''.join(bytes(packet) for packet in packets)
    data_len = len(data)
    img_size = int(math.ceil(math.sqrt(data_len)))

    img_array = np.zeros((img_size, img_size), dtype=np.uint8)

    for i in range(data_len):
        x, y = divmod(i, img_size)
        img_array[x][y] = data[i]

    img = Image.fromarray(img_array)
    img.save(image_file)


def pcap_to_image(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith('.pcap'):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.png")
            process(input_file, output_file)
            print(f"transfer {input_file} to {output_file}")


if __name__ == "__main__":
    input_dir = 'length_output'  # 输入目录，包含 pcap 文件
    output_dir = 'output_images'  # 输出目录，用于保存生成的 PNG 图片
    pcap_to_image(input_dir, output_dir)