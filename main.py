import tkinter as tk
from gacha_logic import draw, show_history

# 创建主界面
root = tk.Tk()
root.title("抽卡模拟器")
root.geometry("400x300")

# 标题
bg_label = tk.Label(root, text="🎴 抽卡模拟器 🎴", font=("Arial", 18))
bg_label.pack(pady=10)

# 按钮
single_draw_btn = tk.Button(root, text="抽 1 次", command=lambda: draw(1, root))
ten_draw_btn = tk.Button(root, text="抽 10 次", command=lambda: draw(10, root))
history_btn = tk.Button(root, text="查看历史记录", command=show_history)

single_draw_btn.pack(pady=5)
ten_draw_btn.pack(pady=5)
history_btn.pack(pady=5)

# 运行主循环
root.mainloop()
