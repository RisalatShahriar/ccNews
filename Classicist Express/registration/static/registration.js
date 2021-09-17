const inputs = document.querySelectorAll(".input");
const link = document.querySelector('#link').value;

function focusFunc() {
  const parent = this.parentNode.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  const parent = this.parentNode.parentNode;

  if (this.value === "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

let loader = function (e) {
  let file = e.target.files;

  let show = "<span>Selected Image: </span>" + file[0].name;

  let output = document.getElementById("selector");
  output.innerHTML = show;
  output.classList.add("active");
};

let fileInput = document.getElementById("file");
fileInput.addEventListener("change", loader);

alert(`registration/${link}`)