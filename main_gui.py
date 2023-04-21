import os
import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from split_to_session import parse_pcap, create_output_files
from normalize_pcap import normalize_pcap
from traffic_to_png import pcap_to_image


def select_pcap():
    global input_file
    input_file = filedialog.askopenfilename(filetypes=[("Pcap files", "*.pcap")])
    if input_file:
        lbl_selected_file.configure(text=f"选择的文件：\n{input_file}")


def process_pcap_in_thread():
    threading.Thread(target=process_pcap).start()


# 定义主要功能函数
def process_pcap():
    if not input_file:
        return

    filename = os.path.basename(input_file).split('.')[0]
    session_output = f'session_output/{filename}'
    length_output = f'length_output/{filename}'
    img_output = f'img_output/{filename}'

    os.makedirs(session_output, exist_ok=True)
    os.makedirs(length_output, exist_ok=True)
    os.makedirs(img_output, exist_ok=True)

    sessions = parse_pcap(input_file)
    create_output_files(sessions, os.path.join(session_output, filename))
    progress['value'] = 33

    normalize_pcap(session_output, length_output, 784)
    progress['value'] = 66

    pcap_to_image(length_output, img_output)
    progress['value'] = 100

    lbl_result.configure(text=f"处理完成！\n已保存到：\n{session_output}\n{length_output}\n{img_output}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pcap Processor")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    lbl_title = tk.Label(frame, text="Pcap 处理工具", font=("Arial", 16))
    lbl_title.pack()

    btn_select = tk.Button(frame, text="选择 Pcap 文件", command=select_pcap)
    btn_select.pack(pady=10)

    lbl_selected_file = tk.Label(frame, text="")
    lbl_selected_file.pack(pady=10)

    btn_process = tk.Button(frame, text="开始处理", command=process_pcap_in_thread)
    btn_process.pack(pady=10)

    progress = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
    progress.pack(pady=10)

    lbl_result = tk.Label(frame, text="")
    lbl_result.pack(pady=10)

    input_file = None

    root.mainloop()
