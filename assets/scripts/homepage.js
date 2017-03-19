$(document).ready(function(){
  var d = new Date();
  var n = d.getHours();
  if (n > 19 || n < 6)
    document.body.className = "day";
  else
    document.body.className = "day";
});
