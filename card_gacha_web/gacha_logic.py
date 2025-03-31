import random
from pool import load_card_pool

card_pool, _ = load_card_pool()

def draw(n=1):
    """ 随机抽卡 """
    results = []
    for _ in range(n):
        rarity = random.choices(["SSR", "SR", "R", "UR"], weights=[10, 25, 60, 15])[0]  # 抽取稀有度
        if card_pool[rarity]:
            results.append(random.choice(card_pool[rarity]))  # 选一张卡片
    return results

HISTORY_FILE = "history.json"

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
    """更新历史记录"""
    history = load_history()
    for card in drawn_cards:
        if card not in history["collected_cards"]:
            history["collected_cards"].append(card)
    save_history(history)