DisplayClock();

function DisplayClock() {
    document.getElementById("timeDisplay").innerHTML = Date();
    setTimeout(DisplayClock, 1000);
}