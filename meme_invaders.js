var screen, input, frames, spFrame, lvFrame;
var alSprite, taSprite, ciSprite;
var aliens, dir, tank, bullets, cities;

function main() {
	display = new Screen(595, 700);
	input = new InputHandler();

	var img = new Image();
	img.addEventListener('load', function() {
		alSprite = [
			[new Sprite(this, 5, 5, 32, 32), new Sprite(this, 5, 5, 32, 32)],
			[new Sprite(this, 5, 47, 32, 32), new Sprite(this, 5, 47, 32, 32)],
			[new Sprite(this, 5, 5, 32, 32), new Sprite(this, 5, 5, 32, 32)]
		];

			taSprite = new Sprite(this, 47, 5, 32, 32);
			ciSprite = new Sprite(this, 47, 47, 32, 32);

			init();
			run();
	});

	img.src = "../sprites/spritesheet.png";
};

function init() {
	frames = 0;
	spFrame = 0;
	lvFrame = 60;
	dir = 1;

	aliens = [];
	var rows = [0, 1, 1, 2, 2];
	for (var i = 0, len = rows.length; i < len; i++) {
		for (var j = 0; j < 10; j++) {
			var a = rows[i];
			aliens.push({
				sprite: alSprite[a],
				x: 35 + j*35,
				y: 35 + i*35,
				w: alSprite[a][0].w,
				h: alSprite[a][0].h

			});
		}
	}
};

function run() {
	var loop = function() {
		update();
		render();
		window.requestAnimationFrame(loop, display.canvas);
	};
	window.requestAnimationFrame(loop, display.canvas);
};

function update() {
	frames++;
	if (frames % lvFrame === 0) {
		spFrame = (spFrame + 1) % 2;

		var _max = 0, _min = screen.width;

		for (var i = 0, len = aliens.length; i < len; i++) {
			var a = aliens[i];
			a.x += 35 * dir;

			_max = Math.max(_max, a.x + a.w);
			_min = Math.min(_min, a.x);
		}
		if (_max > screen.width || _min < 0) {
			dir *= -1;
			for (var i = 0, len = aliens.length; i < len; i++) {
				aliens[i].x += 35 * dir;
				aliens[i].y += 35;
			}
		}
	}
};

function render() {
	display.clear();
	for (var i = 0, len = aliens.length; i < len; i++) {
		var a = aliens[i];
		display.drawSprite(a.sprite[spFrame], a.x, a.y);
	}
};

main();

