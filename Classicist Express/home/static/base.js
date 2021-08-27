// jshint esversion: 6

var time = new Date(Date.now()).toLocaleString().split(',')[0]
const btnHam = document.querySelector(".ham-btn");
const btnTimes = document.querySelector(".times-btn");
const navBar = document.getElementById("nav-bar");
const date = document.getElementById('datetime');

date.innerHTML = time;

function topLeft() {
    const heading = document.querySelector("#topLeftHeading");
    const news = document.querySelector("#topLeftNews");
    const link = document.querySelector("#topLeftLink");
    const picture = document.querySelector("#topLeftPicture");

    fetch(`/api/${document.querySelector("#api").value}`)
    .then(res => res.json())
    .then(data => {
        heading.innerHTML = data.heading[1];
        link.href = `/readmore/${data.link[1]}`;
        news.innerHTML = data.news[1];
        picture.src = `/media/${data.picture[1]}`;
    })
}

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
  this.scrollY > 135
    ? navElement.classList.add("sticky")
    : navElement.classList.remove("sticky");
}

window.addEventListener("scroll", changeCss, false);
topLeft()