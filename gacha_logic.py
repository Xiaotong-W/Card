import random
from pool import load_card_pool
import os
import json

card_pool, _ = load_card_pool()

def draw(n=1):
    """ 随机抽卡 """
    results = []
    for _ in range(n):
        rarity = random.choices(["UR", "SSR", "SR", "R"], weights=[3, 12, 25, 60])[0]
        if card_pool[rarity]:
            card = random.choice(card_pool[rarity])  # card[0]是名称，card[1]是路径
            filename = os.path.basename(card[1])  # 例如：sr_长胡子的人.png
            results.append({
                "name": card[0],  # 卡牌名称：长胡子的人
                "file": filename  # 文件名：sr_长胡子的人.png
            })
    update_history([card["name"] for card in results])  # 仅保存名称到历史记录
    return results

HISTORY_FILE = os.path.join(os.path.dirname(__file__), 'history.json')

def load_history():
    """读取抽卡历史"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"collected_cards": [], "collections": {}}

def save_history(history):
    """保存抽卡历史"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)

def update_history(drawn_cards):
    """更新历史记录（直接使用卡牌名称）"""
    history = load_history()
    for card_name in drawn_cards:  # 直接处理名称
        if card_name not in history["collected_cards"]:
            history["collected_cards"].append(card_name)
    save_history(history)