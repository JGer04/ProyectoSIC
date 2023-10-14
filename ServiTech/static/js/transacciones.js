const btnDiario = document.querySelector("#diario");
const btnMayor = document.querySelector("#mayor");
const btnOcultar = document.querySelector("#ocultarTodo");
const tablaDiario = document.querySelector("#Tdiario");
const tablaMayor = document.querySelector("#Tmayor");

btnDiario.addEventListener("click",  ()=>{
  tablaDiario.classList.add("active");
});

btnMayor.addEventListener("click",  ()=>{
  tablaMayor.classList.add("active");
});

btnOcultar.addEventListener("click", ()=>{
   tablaDiario.classList.remove("active");
   tablaMayor.classList.remove("active");

});
