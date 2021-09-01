// jshint esversion: 6

var time = new Date(Date.now()).toLocaleString().split(',')[0]
const btnHam = document.querySelector(".ham-btn");
const btnTimes = document.querySelector(".times-btn");
const navBar = document.getElementById("nav-bar");
const date = document.getElementById('datetime');
let newsCount = 0;
let currNews = 1;

date.innerHTML = time;

document.addEventListener('DOMContentLoaded', loadtContect())

fetch(`/api/${document.querySelector("#api").value}`)
.then(res => res.json())
.then(data => {
  newsCount = Object.keys(data.heading).length
})

function topLeft() {
  fetch(`/api/${document.querySelector("#api").value}`)
  .then(res => res.json())
  .then(data => {
  if (currNews <= newsCount) {
    const newsDiv = document.querySelector(".container-top-left");
    const article = document.createElement('article');
    const img = document.createElement('img');
    const div = document.createElement('div');
    const heading =document.createElement('h3');
    const news = document.createElement('p');
    const link = document.createElement('a');

    newsDiv.append(article);
    article.append(img);
    article.append(div);
    div.append(heading);
    div.append(news);
    div.append(link);
    heading.innerHTML = data.heading[1];
    link.innerHTML = `Read More <span>>></span>`;
    link.href = `/readmore/${data.link[1]}`;
    news.innerHTML = data.front[1];
    img.src = `/media/${data.picture[1]}`;
    currNews++;
  }
  else {
    return
  }
  })
}

function bottomLeft() {
  fetch(`/api/${document.querySelector("#api").value}`)
  .then(res => res.json())
  .then(data => {
  if (currNews <= newsCount){
    const newsDiv = document.querySelector(".container-bottom-left");
    const article = document.createElement('article');
    const img = document.createElement('img');
    const div = document.createElement('div');
    const heading =document.createElement('h3');
    const news = document.createElement('p');
    const link = document.createElement('a');
    newsDiv.append(article);
    article.append(img);
    article.append(div);
    div.append(heading);
    div.append(news);
    div.append(link);
    heading.innerHTML = data.heading[currNews];
    link.innerHTML = `Read More <span>>></span>`;
    link.href = `/readmore/${data.link[currNews]}`;
    news.innerHTML = data.front[currNews];
    img.src = `/media/${data.picture[currNews]}`;
    currNews++
  }
  else {
    return
  }
  })
}

function right() {
  fetch(`/api/${document.querySelector("#api").value}`)
  .then(res => res.json())
  .then(data => {
  if (currNews <= newsCount) {
    const newsDiv = document.querySelector("#right");
    const article = document.createElement('article');
    const img = document.createElement('img');
    const div = document.createElement('div');
    const heading =document.createElement('h2');
    const news = document.createElement('p');
    const link = document.createElement('a');
    const just = document.createElement('h4');
  
    newsDiv.append(article);
    article.append(just);
    article.append(div);
    div.append(heading);
    div.append(news);
    div.append(link);
    article.append(img);
  
    heading.innerHTML = data.heading[currNews];
    link.innerHTML = `Read More <span>>></span>`;
    link.href = `/readmore/${data.link[currNews]}`;
    news.innerHTML = data.front[currNews];
    img.src = `/media/${data.picture[currNews]}`;
    just.innerHTML = "just in";
    currNews++
  }
  else {
    return
  }
  })
}

function bottom() {
  fetch(`/api/${document.querySelector("#api").value}`)
  .then(res => res.json())
  .then(data => {
  if (currNews <= newsCount) {
    const mainDiv = document.querySelector(".news");
    const sec = document.querySelector(".main-container-left");
    const newsDiv = document.querySelector(".container-bottom-left");
    const article = document.createElement('article');
    const img = document.createElement('img');
    const div = document.createElement('div');
    const heading =document.createElement('h2');
    const news = document.createElement('p');
    const link = document.createElement('a');
  
    mainDiv.append(sec);
    sec.append(newsDiv);
    newsDiv.append(article);
    article.append(div);
    div.append(heading);
    div.append(news);
    div.append(link);
    article.append(img);
  
    heading.innerHTML = data.heading[currNews];
    link.innerHTML = `Read More <span>>></span>`;
    link.href = `/readmore/${data.link[currNews]}`;
    news.innerHTML = data.front[currNews];
    img.src = `/media/${data.picture[currNews]}`;
    currNews++
  }
  else {
    return
  }
  })
}


function loadtContect() {
  for (var i = 0; i<7; i++) {
    right()
    i++
  }
  topLeft()
  for (var i = 0; i<2; i++) {
    bottomLeft()
    i++
  }
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