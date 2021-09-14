let tabButtons = document.querySelectorAll(
  ".tab-container .button-container button"
);

let tabPanels = document.querySelectorAll(".tab-container .tab-panel");

let mq1 = window.matchMedia("(min-width: 802px)");

const showPanel = (i) => {
  tabButtons.forEach((node) => {
    node.style.borderBottom = "none";
  });
  if (mq1.matches) {
    tabButtons[i].style.borderBottom = "2px solid #d7ae66";
  }

  tabPanels.forEach((node) => {
    node.style.display = "none";
  });

  tabPanels[i].style.display = "block";
};
if (mq1.matches) {
  showPanel(0);
}

document.querySelector(".view").addEventListener("click", function () {
  document.querySelector(".single-user").classList.toggle("expand");
});
