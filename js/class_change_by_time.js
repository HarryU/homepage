var d = new Date();
var n = d.getHours();
if (n > 19 || n < 6) {
    document.body.className = "night";
		document.getElementById("mainbox").classList.add("night");
		document.getElementById("mainbox").classList.remove("day");
}
else {
    document.body.className = "day";
		document.getElementById("mainbox").classList.remove("night");
		document.getElementById("mainbox").classList.add("day");
}
