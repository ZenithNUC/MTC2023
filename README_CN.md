# MTC2023

本项目是对开源项目 [USTC-TK2016](https://github.com/yungshenglu/USTC-TK2016) 的重写和增强。在此对 USTC-TK2016 的开发者表示感谢。Pcap 预处理工具是一个简单的基于 Python 的工具，用于将 pcap 文件预处理成图像，以便进行网络流量分析和机器学习。该工具实现了 pcap 文件的拆分、规范化和转换为 PNG 图像。

[English Documentation](./README_EN.md)

## 功能

1. 将 pcap 文件分割为会话并隐去
2. 规范化 pcap 文件（固定长度）
3. 将 pcap 文件转换为灰度 PNG 图像

## 文件结构

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

## 如何运行

### 环境配置

1. 安装 Python 3.x
2. 安装依赖：`pip install -r requirements.txt`

### 运行项目

执行主 GUI 脚本：`python main_gui.py`

### 运行单个脚本

1. 将 pcap 分割为会话：修改文件中路径参数`input_file`和`output_folder`并运行`python split_to_session.py`
2. 规范化 pcap 文件：修改文件中路径参数`input_folder`和`output_folder`并运行`python normalize_pcap.py`
3. 将 pcap 转换为 PNG：修改文件中路径参数`input_folder`和`output_folder`并运行`python traffic_to_png.py`

## 依赖库

- Scapy
- NumPy
- Pillow
- tkinter

## 许可证

本项目使用 MIT 许可证。有关详细信息，请参阅 [LICENSE](./LICENSE) 文件。
