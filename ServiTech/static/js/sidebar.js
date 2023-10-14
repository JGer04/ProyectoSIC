const btnToggle = document.querySelector(".toggle-btn");
const contenedor = document.querySelector(".content");

btnToggle.addEventListener("click", function () {
  document.getElementById("sidebar").classList.toggle("active");
  contenedor.classList.toggle("content-active");
});
