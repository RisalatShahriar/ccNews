let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", ()=>{
  sidebar.classList.toggle("open");
  menuBtnChange();//calling the function(optional)
});

sidebar.classList.toggle("open");
  menuBtnChange();

// following are the code to change sidebar button(optional)
function menuBtnChange() {
 if(sidebar.classList.contains("open")){
   closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
 }else {
   closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the iocns class
 }
}
$(".profile").click(function(){
  $.get("./api/logout.php",function(data){
    var res = JSON.parse(data);
    if (res.msg=="C005") {
      window.location.replace("./");
    }
  });
});

var current_location = window.location.pathname;

$(document).ready(function(){
  var locp = current_location.split("/");
  var loc = locp[locp.length-1].toLowerCase();
  if (loc=="News") {
    
  }

  switch(loc) {
    case "news":
      $("#nav_news").addClass("active");
      break;
    case "settings":
      $("#nav_settings").addClass("active");
      break;
    case "users":
      $("#nav_users").addClass("active");
      break;
    default:
      $("#nav_dashboard").addClass("active");
  } 
});