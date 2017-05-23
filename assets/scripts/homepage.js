var image_urls = [];
$.getJSON("https://www.reddit.com/r/softwaregore+programmerhumor+itsaunixsystem/.json", function(data) {
	$.each(data.data.children, function(i,item){
		url = item.data.url;
		if (((url.includes('.jpg')) || (url.includes('.gif')) || (url.includes('.png'))) && ((!url.includes('.gifv'))))
		{
			url = url.replace('http:', 'https:');
			image_urls.push(url);
		}
	});
	var slides = new Array();

	var i;
	for (i = 0; i < image_urls.length; i++) {
		slides[i] = new Image();
		slides[i].src = image_urls[i];
	}

	var slideIndex = 0;
	showSlides();

	function showSlides() {
		if (!document.images) {return};
		document.getElementById('slide').src = slides[slideIndex].src;
		slideIndex++;
		if (slideIndex == slides.length) { slideIndex = 1 }
		setTimeout(showSlides, 25000);
	}
});

$(document).ready(function(){
	var d = new Date();
	var n = d.getHours();
	if (n > 19 || n < 6)
		document.body.className = "day";
	else
		document.body.className = "day";
});
