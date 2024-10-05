

function myfunct() {
 alert("ПРИВЕТ!!!");
}


function doSomethingCool(event) {
 setInterval(() => window.location.reload(true), 1000); // Просто и эффективно обновление страницы каждую 1 сек
}


function currentTime() {
    var date = new Date()
    date = convertTZ(date, "Asia/Almaty")
    var hour = date.getHours();
    var min = date.getMinutes();
    var sec = date.getSeconds();
    hour = updateTime(hour);
    min  = updateTime(min);
    sec  = updateTime(sec);
    document.getElementById("timer").textContent = hour + " : " + min + " : " + sec;
    var t = setTimeout(currentTime, 1000);
 }

function convertTZ(date, tzString) {
    return new Date((typeof date === "string" ? new Date(date) : date).toLocaleString("en-US", {timeZone: tzString}));
}

function updateTime(k) {
    return k < 10 ? "0" + k : k;
}

currentTime();