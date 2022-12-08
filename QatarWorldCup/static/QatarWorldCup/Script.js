function getDateNow() {
    date = new Date();
    year = date.getFullYear();
    month = date.getMonth() + 1;
    day = date.getDate();
    document.getElementById("NowDate").innerHTML = month + "/" + day + "/" + year;
}