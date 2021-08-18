// jshint esversion: 6

const btnHam = document.querySelector(".ham-btn");
const btnTimes = document.querySelector(".times-btn");
const navBar = document.getElementById("nav-bar");

btnHam.addEventListener("click", function () {
  if (btnHam.className !== "") {
    btnHam.style.display = "none";
    btnTimes.style.display = "block";
    navBar.classList.add("show-nav");
  }
});

btnTimes.addEventListener("click", function () {
  if (btnHam.className !== "") {
    this.style.display = "none";
    btnHam.style.display = "block";
    navBar.classList.remove("show-nav");
  }
});

function changeCss() {
  var bodyElement = document.querySelector("body");
  var navElement = document.querySelector(".nav-bar");
  this.scrollY > 70
    ? navElement.classList.add("sticky")
    : navElement.classList.remove("sticky");
}

window.addEventListener("scroll", changeCss, false);
