$(".nav-tabs > li").click(function(){
	$(".nav-tabs > li").each(function(){
		$(this).removeClass("active");
	});
	$(".nav-targets").each(function(){
		$(this).css("display","none");
	});
	$(this).addClass("active");

	var target = $(this).attr("nav-target");

	$(`#${target}`).css("display","block");

	// alert($(this).attr("nav-target"));
});

$(document).ready(function(){
	$(".nav-tabs > li").first().click();
});