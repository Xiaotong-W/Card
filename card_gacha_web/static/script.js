function drawCard(n) {
    fetch(`/draw/${n}`)
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById("result");
        resultDiv.innerHTML = "";  // 清空之前的结果

        data.forEach(card => {
            let cardDiv = document.createElement("div");
            cardDiv.className = "card";

            let img = document.createElement("img");
            img.src = card[1];  // 使用卡片的图片路径
            img.alt = card[0];

            let text = document.createElement("p");
            text.textContent = `🎴 ${card[0]}`;

            cardDiv.appendChild(img);
            cardDiv.appendChild(text);
            resultDiv.appendChild(cardDiv);
        });
    });
}
