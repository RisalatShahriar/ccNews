// jshint esversion: 6
const btnHam = document.querySelector(".ham-btn");
const btnTimes = document.querySelector(".times-btn");
const navBar = document.getElementById("nav-bar");
let currentNews = 1;

document.addEventListener('DOMContentLoaded', () => {
  topLeft();
  bottomLeft();
  for (var i = 0; i<5; i++){
    right();
  }
  for (var i = 0; i<5; i++){
    bottom();
  }
  if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
    for (var i = 0; i<5; i++){
      bottom();
    }
  }
})

function topLeft() {
  fetch(`/api/${document.querySelector("#api").value}/top`)
  .then(res => res.json())
  .then(data => {
    if (Object.keys(data.heading).length > 2) {
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
    }
  })  
}//Top Stories

function bottomLeft() {
  fetch(`/api/${document.querySelector("#api").value}/top`)
  .then(res => res.json())
  .then(data => {
    if (Object.keys(data.heading).length > 2) {
      for (var i = 0; i<2; i++){
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
        heading.innerHTML = data.heading[i+2];
        link.innerHTML = `Read More <span>>></span>`;
        link.href = `/readmore/${data.link[i+2]}`;
        news.innerHTML = data.front[i+2];
        img.src = `/media/${data.picture[i+2]}`;
      }
    }
  })
}//Top Stories bottom

function right() {
  fetch(`/api/${document.querySelector("#api").value}`)
  .then(res => res.json())
  .then(data => {
    if (Object.keys(data.heading).length >= currentNews) {
      const newsDiv = document.querySelector("#right");
      const article = document.createElement('article');
      const img = document.createElement('img');
      const div = document.createElement('div');
      const heading =document.createElement('h2');
      const news = document.createElement('p');
      const link = document.createElement('a');
      
      newsDiv.append(article);
      article.append(div);
      div.append(heading);
      div.append(news);
      div.append(link);
      article.append(img);
      
      heading.innerHTML = data.heading[currentNews];
      link.innerHTML = `Read More <span>>></span>`;
      link.href = `/readmore/${data.link[currentNews]}`;
      news.innerHTML = data.front[currentNews];
      img.src = `/media/${data.picture[currentNews]}`; 
      currentNews++;
    }
    else {
      return;
    }
  })
}//Latest Stories

function bottom() {
  fetch(`/api/${document.querySelector("#api").value}`)
  .then(res => res.json())
  .then(data => {
    if (Object.keys(data.heading).length >= currentNews) {
      const newsDiv = document.querySelector("#bottom");
      const article = document.createElement('article');
      const img = document.createElement('img');
      const div = document.createElement('div');
      const heading =document.createElement('h3');
      const news = document.createElement('p');
      const link = document.createElement('a');
      newsDiv.append(article);
      article.append(div);
      div.append(img);
      div.append(heading);
      div.append(news);
      div.append(link);
      heading.innerHTML = data.heading[currentNews];
      link.innerHTML = `Read More <span>>></span>`;
      link.href = `/readmore/${data.link[currentNews]}`;
      news.innerHTML = data.front[currentNews];
      img.src = `/media/${data.picture[currentNews]}`;
      currentNews++;
    }
    else {
      return
    }
  })
}//News

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
