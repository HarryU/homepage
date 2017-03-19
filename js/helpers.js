function Bullet(x, y, vy, w, h, colour) {
	this.x = x;
	this.y = y;
	this.vy = vy;
	this.w = w;
	this.h = h;
	this.colour = colour;
}

Bullet.prototype.update = function() {
	this.y += this.vy;
}

function Screen(width, height) {
	this.canvas = document.createElement("canvas");
	this.canvas.width = this.width = width;
	this.canvas.height = this.height = height;
	this.ctx = this.canvas.getContext("2d");
	document.body.appendChild(this.canvas);
};

Screen.prototype.drawSprite = function(sp, x, y) {
	this.ctx.drawImage(sp.img, sp.x, sp.y, sp.w, sp.h, x, y, sp.w, sp.h);
};

Screen.prototype.clear = function() {
	this.ctx.clearRect(0, 0, this.width, this.height);	
};

Screen.prototype.drawBullet = function(bullet) {
	this.ctx.fillStyle = bullet.colour;
	this.ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
};

function Sprite(img, x, y, w, h) {
	this.img = img;
	this.x = x;
	this.y = y;
	this.w = w;
	this.h = h;
};

function InputHandler() {
	this.down = {};
	this.pressed = {};

	var _this = this;
	document.addEventListener("keydown", function(evt) {
		_this.down[evt.keyCode] = true;
	});

	document.addEventListener("keyup", function(evt) {
		delete _this.down[evt.keyCode];
		delete _this.pressed[evt.keyCode];
	});
};

InputHandler.prototype.isDown = function(code) {
	return this.down[code];
};

InputHandler.prototype.isPressed = function(code) {
	if (this.down[code]) {
		return false;
	} else if (this.pressed[code]) {
		return this.pressed[code];
	}
};

