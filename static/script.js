// script.js
function drawCard(n) {
    fetch(`/draw/${n}`)
        .then(response => response.json())
        .then(data => {
            let html = '<div class="results-grid">';
            data.forEach(card => {
                const rarityClass = card.file.split('_')[0].toLowerCase();
                html += `
                <div class="result-card ${rarityClass}">
                    <div class="card-frame">
                        <img src="/static/images/${card.file}"
                             alt="${card.name}"
                             class="card-image"
                             data-rarity="${rarityClass.toUpperCase()}">
                    </div>
                    <p class="card-name">${card.name}</p>
                </div>`;
            });
            html += '</div>';
            document.getElementById("result").innerHTML = html;
        });
}