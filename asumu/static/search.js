function searchroom() {
    let sr = document.getElementById('sr').value;
    console.log("検索ワード:", sr);

    fetch("/searchroom", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ roomname: sr })
    })
    .then(response => response.json())  // JSON を受け取る
    .then(data => {
        console.log("検索結果:", data);
        let resultContainer = document.getElementById("search-results");
        resultContainer.innerHTML = ""; // 検索結果をクリア

        if (data.length === 0) {
            resultContainer.innerHTML = "<p>部屋が見つかりませんでした。</p>";
            return;
        }

        data.forEach(room => {
            let roomElement = document.createElement("div");
            roomElement.innerHTML = `
                <h3>${room.name}</h3>
                <div class="display">
                    <div class="circle1"></div>
                    <div id="create">
                        <button onclick="inroom('${ room.name }')">入室</button>
                    </div>
                </div>
                <hr>
            `;
            resultContainer.appendChild(roomElement);
        });
    })
    .catch(error => console.error("エラー:", error));
}
