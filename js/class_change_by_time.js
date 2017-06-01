var d = new Date();
var n = d.getHours();
if (n > 19 || n < 6) {
    document.body.className = "night animated";
		document.getElementById("bg").classList.add("night");
		document.getElementById("bg").classList.remove("day");
		document.getElementById("mainbox").classList.add("night");
		document.getElementById("mainbox").classList.remove("day");
    var buttons =document.getElementsByName("button");
		for (var i = 0; i < buttons.length; i++) {
			buttons[i].classList.remove("day");
			buttons[i].classList.add("night");
		}
}
else {
    document.body.className = "day";
		document.getElementById("mainbox").classList.remove("night");
		document.getElementById("mainbox").classList.add("day");
    var buttons =document.getElementsByName("button");
		for (var i = 0; i < buttons.length; i++) {
			buttons[i].classList.remove("night");
			buttons[i].classList.add("day");
		}
}
