// static/script.js
function drawCard(n) {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = '<div class="loading"></div>';

    fetch(`/draw/${n}`)
        .then(response => response.json())
        .then(data => {
            let html = '';
            data.forEach(card => {
                html += `
                <div class="card-result" data-rarity="${getRarity(card.file)}">
                    <img src="/static/images/${card.file}" alt="${card.name}">
                    <p>${card.name}</p>
                </div>`;
            });
            resultDiv.innerHTML = html;

            // 添加入场动画
            setTimeout(() => {
                document.querySelectorAll('.card-result').forEach(el => {
                    el.style.opacity = 1;
                    el.style.transform = 'scale(1)';
                });
            }, 50);
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = '<p class="error">抽卡失败，请稍后重试</p>';
        });
}

// 获取稀有度标识
function getRarity(filename) {
    return filename.split('_')[0].toUpperCase();
}