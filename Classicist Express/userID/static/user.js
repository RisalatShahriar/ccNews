let tabButtons = document.querySelectorAll(
  ".tab-container .button-container button"
);

let tabPanels = document.querySelectorAll(".tab-container .tab-panel");

let mq = window.matchMedia("(min-width: 800px)");

const showPanel = (i) => {
  if (mq.matches) {
    tabButtons.forEach((node) => {
      node.style.borderBottom = "none";
    });
    tabButtons[i].style.borderBottom = "2px solid #d7ae66";
    tabPanels.forEach((node) => {
      node.style.display = "none";
    });

    tabPanels[i].style.display = "block";
  }
};

if (mq.matches) {
  showPanel(0);
}