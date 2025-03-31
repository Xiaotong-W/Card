import os
import json

IMAGE_FOLDER = "static/images"
RARITY_PREFIX = {"UR": "ur_", "SSR": "ssr_", "SR": "sr_", "R": "r_"}


def load_card_pool(image_folder=IMAGE_FOLDER):
    """ 自动读取 images 文件夹并构建卡池 """
    # 确保包含所有稀有度
    card_pool = {"UR": [], "SSR": [], "SR": [], "R": []}  # 初始化时包含 UR

    if not os.path.exists(image_folder):
        print("⚠️ 图片文件夹不存在！")
        return card_pool, {}

    for filename in os.listdir(image_folder):
        if filename.endswith((".png", ".jpg")):  # 兼容 PNG & JPG
            for rarity, prefix in RARITY_PREFIX.items():
                if filename.startswith(prefix):  # 检查稀有度是否匹配
                    card_name = filename.replace(".png", "").replace(".jpg", "").replace(prefix, "").capitalize()
                    card_pool[rarity].append((card_name, os.path.join(image_folder, filename)))

    collections = load_collections()  # 读取套卡
    return card_pool, collections


COLLECTIONS_FILE = "collections.json"


def load_collections():
    """ 读取套卡数据 """
    if not os.path.exists(COLLECTIONS_FILE):
        return {}

    with open(COLLECTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    pool, sets = load_card_pool()
    print("卡池信息:", pool)
    print("套卡信息:", sets)
