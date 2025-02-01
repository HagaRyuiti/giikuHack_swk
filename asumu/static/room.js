function inroom(roomname) {
    console.log("入室する部屋:", roomname);

    fetch("/room", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ roomname: roomname })
    })
    .then(response => response.json())  // サーバーから JSON を取得
    .then(data => {
        if (data.status === "success") {
            window.location.href = `/room/${encodeURIComponent(roomname)}`;  // 部屋ページへリダイレクト
        } else {
            alert("部屋に入室できませんでした。");
        }
    })
    .catch(error => console.error("エラー:", error));
}
