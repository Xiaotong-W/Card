import os

# 稀有度前缀映射（文件名必须以这些前缀开头）
RARITY_PREFIX = {
    "SSR": "ssr_",
    "SR": "sr_",
    "R": "r_",
    "UR": "ur_"
}


def load_card_pool(image_folder="images"):
    """ 自动读取 images 文件夹并构建卡池 """
    card_pool = {"SSR": [], "SR": [], "R": [], "UR": []}

    if not os.path.exists(image_folder):
        print("⚠️ 图片文件夹不存在！")
        return card_pool

    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):  # 处理 PNG 和 JPG
            for rarity, prefix in RARITY_PREFIX.items():
                if filename.lower().startswith(prefix):  # 忽略大小写
                    card_name = filename.replace(prefix, "").rsplit(".", 1)[0].capitalize()
                    card_pool[rarity].append((card_name, os.path.join(image_folder, filename)))

    return card_pool


# 让 `pool.py` 可独立运行查看卡池
if __name__ == "__main__":
    pool = load_card_pool()
    for rarity, cards in pool.items():
        print(f"{rarity}: {cards}")
