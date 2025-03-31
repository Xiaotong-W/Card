import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pool import load_card_pool  # 载入卡池
import os
# 载入卡池
CARD_POOL = load_card_pool()

# 定义抽取概率
PROBABILITIES = {
    "SSR": 0.15,  # 5%
    "SR": 0.30,   # 25%
    "R": 0.50,     # 70%
    "UR": 0.05
}

history = []  # 记录抽卡历史


def draw(times, root):
    """ 执行抽卡 """
    results = []
    for _ in range(times):
        rarity = random.choices(list(PROBABILITIES.keys()), weights=PROBABILITIES.values())[0]
        if CARD_POOL[rarity]:  # 确保该稀有度有卡
            card = random.choice(CARD_POOL[rarity])
            results.append(card)
            history.append(card)  # 记录抽卡结果

    show_results(results, root)


def show_results(results, root, max_width=600, max_height=900):
    """ 显示抽卡结果，限制图片的最大尺寸 """
    result_window = tk.Toplevel(root)
    result_window.title("抽卡结果")

    for card_name, img_path in results:
        frame = tk.Frame(result_window)
        frame.pack(pady=5)

        try:
            abs_path = os.path.abspath(img_path)
            pil_img = Image.open(abs_path)

            # 获取图片原始尺寸
            width, height = pil_img.size

            # 计算缩放比例
            ratio = min(max_width / width, max_height / height)

            # 计算新的尺寸
            new_width = int(width * ratio)
            new_height = int(height * ratio)

            # 缩放图片
            pil_img = pil_img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            img = ImageTk.PhotoImage(pil_img)

            label_img = tk.Label(frame, image=img)
            label_img.image = img
            label_img.pack()

        except Exception as e:
            label_text = tk.Label(frame, text=f"⚠️ 图片加载失败: {card_name}", font=("Arial", 12))
            label_text.pack()
            print(f"图片加载失败: {img_path}, 错误: {e}")

        label_text = tk.Label(frame, text=f"🎴 {card_name}", font=("Arial", 12))
        label_text.pack()


def show_history():
    """ 显示抽卡历史 """
    history_window = tk.Toplevel()
    history_window.title("抽卡历史")

    if not history:
        messagebox.showinfo("历史记录", "尚未抽到任何卡片！")
        return

    for card_name, _ in history:
        label = tk.Label(history_window, text=f"🎴 {card_name}", font=("Arial", 12))
        label.pack()
