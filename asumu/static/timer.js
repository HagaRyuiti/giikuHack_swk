var startButton;    // startボタン
var stopButton;     // stopボタン
var resetButton;    // resetボタン
var showTime;       // 表示時間

var timer;              // setinterval, clearTimeoutで使用
var startTime;          // 開始時間
var elapsedTime = 0;    // 経過時間
var holdTime = 0;       // 一時停止用に時間を保持

window.onload = function () {
    startButton = document.getElementById("start");
    stopButton = document.getElementById("stop");
    resetButton = document.getElementById("reset");
    showTime = document.getElementById("time");
}

// スタートボタン押下時
function start(){
    // 開始時間を現在の時刻に設定
    startTime = Date.now();

    // 時間計測
    measureTime();

    startButton.disabled = true;
    stopButton.disabled = false;
    resetButton.disabled = false;
}

// ストップボタン押下時
function stop(){
    // タイマー停止
    clearInterval(timer);

    // 停止時間を保持
    holdTime += Date.now() - startTime;

    startButton.disabled = false;
    stopButton.disabled = true;
    resetButton.disabled = false;
    
}

// リセットボタン押下時
function reset(){
    // タイマー停止
    clearInterval(timer);

    // 変数、表示を初期化
    elapsedTime = 0;
    holdTime = 0;
    showTime.textContent = "00:00:00";

    startButton.disabled = false;
    stopButton.disabled = true;
    resetButton.disabled = true;
}

// 時間を計測（再帰関数）
function measureTime() {
    // タイマーを設定
    timer = setTimeout(function () {
        // 経過時間を設定し、画面へ表示
        elapsedTime = Date.now() - startTime + holdTime;
        showTime.textContent = new Date(elapsedTime).toISOString().slice(11, 20);
        // 関数を呼び出し、時間計測を継続する
        measureTime()
        return {
            elapsedTime,
        };
    }, 10);
}

//時間を保存する
function save() {
    
    //今までの時間のデータを持ってくる
    function greet(callback) {
        fetch("/getsave", { method: "GET"})
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(madetime => {
                console.log(madetime[0]);
                console.log(elapsedTime);
                Imadetime = parseInt(madetime[0]) / 1000;
                IelapasedTime = parseInt(elapsedTime) / 1000;
                Mmadetime = Math.trunc(Imadetime);
                MelapasedTime = Math.trunc(IelapasedTime);
                console.log(Mmadetime);
                console.log(MelapasedTime)
                tasutime = Mmadetime + MelapasedTime
                console.log(tasutime);
                callback(tasutime);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }
        
    // フォームをサーバーに送信する方法
    function savesave(tasutime){
        console.log(tasutime)
        data = tasutime
        fetch("/createsave", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
        body: JSON.stringify({ savetime: data })
        })
        .then(response => {
            if (response.ok) {
                window.location.href = "/home"; // 作成後、ホームページにリダイレクト
            } else {
                alert("時間の保存に失敗しました");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("エラーが発生しました");
        });
        }

        greet(savesave);

        }