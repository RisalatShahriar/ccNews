// jshint esversion:6
const inputs = document.querySelectorAll(".input");

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