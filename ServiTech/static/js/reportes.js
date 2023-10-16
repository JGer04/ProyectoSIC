const btnER = document.querySelector(".estado-resultados");
const divER = document.querySelector(".resultados");
const btnEC = document.querySelector(".estado-capital");
const divEC = document.querySelector(".capital");
const btnBG = document.querySelector(".balance-general");
const divBG = document.querySelector(".general");
const btnCerrar = document.querySelector(".cerrar-ef");

btnER.addEventListener("click", ()=> {
 divER.classList.add("mostrar");
})

btnEC.addEventListener("click", ()=> {
 divEC.classList.add("mostrar");
})

btnBG.addEventListener("click", ()=> {
 divBG.classList.add("mostrar");
})

btnCerrar.addEventListener("click", ()=> {
 divER.classList.remove("mostrar");
 divEC.classList.remove("mostrar");
 divBG.classList.remove("mostrar");
})