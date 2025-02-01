function login() {
    let un = document.getElementById('username').value;
    let pw = document.getElementById('password').value;
    
    // フォームをサーバーに送信する方法
    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: un, password: pw })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "/home"; // 作成後、ホームページにリダイレクト
        } else {
            alert("ログインに失敗しました");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("エラーが発生しました");
    });
}
