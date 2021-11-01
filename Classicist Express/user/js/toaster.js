function toaster(text,sec=3) {
  // Get the toaster DIV
  var x = $("toaster");

  x.html(text);

  // Add the "show" class to DIV
  x.addClass("show");

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.removeClass("show"); }, sec*1000);
}