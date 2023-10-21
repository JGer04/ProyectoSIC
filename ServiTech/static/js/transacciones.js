const btnDiario = document.querySelector("#diario");
const btnOcultar = document.querySelector("#ocultarTodo");
const tablaDiario = document.querySelector("#Tdiario");

btnDiario.addEventListener("click",  ()=>{
  tablaDiario.classList.add("active");
});

btnOcultar.addEventListener("click", ()=>{
   tablaDiario.classList.remove("active");
});
