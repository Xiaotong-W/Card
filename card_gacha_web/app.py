from flask import Flask, render_template, jsonify
from gacha_logic import draw

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
    all_cards = {rarity: [(name, f"/static/images/{file}") for name, file in cards] for rarity, cards in
                 card_pool.items()}

    return render_template("gallery.html", all_cards=all_cards, owned_cards=owned_cards)


@app.route("/collections")
def collections():
    """ 展示所有套卡及收集进度 """
    return render_template("collections.html", collections=collections, owned_cards=owned_cards)


if __name__ == "__main__":
    app.run(debug=True)
