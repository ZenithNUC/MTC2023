# MTC2023

This project is a rewrite and enhancement of the open-source project [USTC-TK2016](https://github.com/yungshenglu/USTC-TK2016). I would like to express my gratitude to the developers of USTC-TK2016 for their great work. Pcap Preprocessing Tool is a simple Python-based tool for preprocessing pcap files into images for network traffic analysis and machine learning purposes. The tool implements pcap file splitting, normalization, and conversion to PNG images.

[中文版文档](./README_CN.md)

## Features

1. Split pcap files into sessions
2. Normalize pcap files (fixed length)
3. Convert pcap files to grayscale PNG images

## File Structure

```path
.
├─ main_gui.py
├─ normalize_pcap.py
├─ split_to_session.py
├─ traffic_to_png.py
├─ img_output
├─ length_output
└─ session_output
```

## How to Run

### Environment Setup

1. Install Python 3.x
2. Install dependencies: `pip install -r requirements.txt`

### Run the project

Execute the main GUI script: `python main_gui.py`

### Run individual scripts

1. Split pcap to sessions: Change path value `input_file` and `output_folder` in file and run`python split_to_session.py`
2. Normalize pcap files: Change path value `input_folder` and `output_folder` in file and run`python normalize_pcap.py`
3. Convert pcap to PNG: Change path value `input_folder` and `output_folder` in file and run`python traffic_to_png.py`

## Dependencies

- Scapy
- NumPy
- Pillow
- tkinter

## License

This project is licensed under the MIT License.Please read [LICENSE](./LICENSE).
