const hamburger = document.getElementById("hamburger");
const mobileNav = document.getElementById("toggle-nav");

hamburger.onclick = function () {
  mobileNav.classList.toggle("hide-nav");
};
