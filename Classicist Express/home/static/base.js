// jshint esversion: 6

var time = new Date(Date.now()).toLocaleString().split(',')[0]
const btnHam = document.querySelector(".ham-btn");
const btnTimes = document.querySelector(".times-btn");
const navBar = document.getElementById("nav-bar");
const date = document.getElementById('datetime');

date.innerHTML = time;

function topLeft() {
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

    fetch(`/api/${document.querySelector("#api").value}`)
    .then(res => res.json())
    .then(data => {
        heading.innerHTML = data.heading[1];
        link.innerHTML = `Read More <span>>></span>`;
        link.href = `/readmore/${data.link[1]}`;
        news.innerHTML = data.front[1];
        img.src = `/media/${data.picture[1]}`;
    })
}

function bottomLeft() {
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

    fetch(`/api/${document.querySelector("#api").value}`)
    .then(res => res.json())
    .then(data => {
      heading.innerHTML = data.heading[1];
      link.innerHTML = `Read More <span>>></span>`;
      link.href = `/readmore/${data.link[1]}`;
      news.innerHTML = data.front[1];
      img.src = `/media/${data.picture[1]}`;
    })
}

function right() {
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

  fetch(`/api/${document.querySelector("#api").value}`)
  .then(res => res.json())
  .then(data => {
    heading.innerHTML = data.heading[1];
    link.innerHTML = `Read More <span>>></span>`;
    link.href = `/readmore/${data.link[1]}`;
    news.innerHTML = data.front[1];
    img.src = `/media/${data.picture[1]}`;
    just.innerHTML = "just in";
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
