from flask import Flask, render_template, jsonify
from gacha_logic import draw, load_history  # 导入 load_history
from pool import load_card_pool
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/draw/<int:n>")
def gacha_draw(n):
    results = draw(n)
    return jsonify(results)  # 以 JSON 格式返回


@app.route("/gallery")
def gallery():
    """ 展示所有卡牌，包括已抽到和未抽到的 """
    all_cards, _ = load_card_pool()

    # 获取用户已经拥有的卡片
    history = load_history()
    owned_cards = history["collected_cards"]

    return render_template("gallery.html", all_cards=all_cards, owned_cards=owned_cards)


@app.route("/collections")
def collections():
    history = load_history()
    owned_cards = {name.strip().lower() for name in history["collected_cards"]}  # 统一小写
    _, collections = load_card_pool()
    return render_template("collections.html", collections=collections, owned_cards=owned_cards)

if __name__ == "__main__":
    app.run(debug=True)

