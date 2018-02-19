var canvas = $("#c");
var c = canvas[0].getContext("2d");

var lettuce_path = "assets/images/lettuce1600.png";
var tomato_path = "assets/images/tomato.png";
var onion_path = "assets/images/onion.png";

var images = new Array();

var loop = setInterval(function() {
	c.fillStyle = "lightblue";
	c.fillRect(0, 0, 500, 500);
	DrawRectangle('lightgreen', 50, 50, 100, 100);
	DrawRectangle('red', 150, 50, 100, 100);
    DrawRectangle('purple', 250, 50, 100, 100);
	for (var i =  0; i < images.length; i++) {
		images[i].update();
	}
}, 30);

var mouseX = 0,
		mouseY = 0;
var mousePressed = false;
var dragging = false;
canvas.mousemove(function(e) {
	mouseX = e.offsetX;
	mouseY = e.offsetY;
});

$(document).mousedown(function() {
	mousePressed = true;
    if (mouseX < 350 && mouseX > 250 && mouseY < 150 && mouseY > 50) {
        new_img = new DragImage(onion_path, mouseX, mouseY);
        images.push(new_img);
    }
	if (mouseX < 250 && mouseX > 150 && mouseY < 150 && mouseY > 50) {
		new_img = new DragImage(tomato_path, mouseX, mouseY);
		images.push(new_img);
	}
	if (mouseX < 150 && mouseX > 50 && mouseY < 150 && mouseY > 50) {
		new_img = new DragImage(lettuce_path, mouseX, mouseY);
		images.push(new_img);
	}
}).mouseup(function() {
	mousePressed = false;
	dragging = false;
});

function DrawRectangle(colour, upper, lower, leftmost, rightmost) {
	c.beginPath();
	c.rect(upper, lower, leftmost, rightmost);
	c.fillStyle = colour;
	c.fill();
}

function DragImage(src, x, y) {
	var that = this;
	var startX = 0,
	startY = 0;
	var drag = false;

	this.x = x;
	this.y = y;
	var img = new Image();
	img.src = src;
	img.height = 50;
	img.width = 50;
	this.update = function() {
		if (mousePressed ) {

			var left = that.x;
			var right = that.x + img.width;
			var top = that.y;
			var bottom = that.y + img.height;
			if (!drag) {
				startX = mouseX - that.x;
				startY = mouseY - that.y;
			}
			if (mouseX < right && mouseX > left && mouseY < bottom && mouseY > top) {
				if (!dragging){
					dragging = true;
					drag = true;
				}

			}

		} else {

			drag = false;
		}
		if (drag) {
			that.x = mouseX - startX;
			that.y = mouseY - startY;
		}
		c.drawImage(img, that.x, that.y, 50, 50);
	}
}
