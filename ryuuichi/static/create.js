function createroom() {
    let rn = document.getElementById('rn').value;
    console.log(rn);
    
    // フォームをサーバーに送信する方法
    fetch("{{ url_for('createroom') }}", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ roomname: rn })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "{{ url_for('home') }}"; // 作成後、ホームページにリダイレクト
        } else {
            alert("部屋の作成に失敗しました");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("エラーが発生しました");
    });
}
