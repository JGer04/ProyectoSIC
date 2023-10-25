const celdasMontosCI = document.querySelectorAll(".monto-CI");
const btnActualizar = document.querySelector(".actualizarMonto-CI")
let celdasMontosCI2, valores2 = [];

const celdasTabla2 = document.querySelectorAll(".tabla2");
const btnTabla2 = document.querySelector(".actualizarTabla2")
let valoresTabla2, valores3 = [];

const celdasTabla3 = document.querySelectorAll(".tabla3");
const btnTabla3 = document.querySelector(".actualizarTabla3")
let valoresTabla3, valores4 = [];

const celdasTabla4 = document.querySelectorAll(".tabla4");
const btnTabla4 = document.querySelector(".actualizarTabla4")
let valoresTabla4, valores5 = [];

function reiniciarMontos(arrModificar) {
      arrModificar.forEach(function(celda) {
      celda.textContent = '0';
    });
  }

function mostrarMontos(arrModificar, arrValores) {
    arrModificar.forEach((celda, i) => {
     celda.textContent = arrValores[i];
    });
  }


document.addEventListener('DOMContentLoaded', function() {
    celdasMontosCI2 = [...celdasMontosCI];
    celdasMontosCI2.forEach((monto,i) =>{
     valores2[i] = monto.textContent;
    })
    reiniciarMontos(celdasMontosCI);

    valoresTabla2 = [...celdasTabla2];
    valoresTabla2.forEach((monto,i) =>{
     valores3[i] = monto.textContent;
    })
    reiniciarMontos(celdasTabla2);

    valoresTabla3 = [...celdasTabla3];
    valoresTabla3.forEach((monto,i) =>{
     valores4[i] = monto.textContent;
    })
    reiniciarMontos(celdasTabla3);

    valoresTabla4 = [...celdasTabla4];
    valoresTabla4.forEach((monto,i) =>{
     valores5[i] = monto.textContent;
    })
    reiniciarMontos(celdasTabla4);
  })

btnActualizar.addEventListener("click", ()=>{
 mostrarMontos(celdasMontosCI,valores2);
})

btnTabla2.addEventListener("click", ()=>{
 mostrarMontos(celdasTabla2,valores3);
})

btnTabla3.addEventListener("click", ()=>{
 mostrarMontos(celdasTabla3,valores4);
})

btnTabla4.addEventListener("click", ()=>{
 mostrarMontos(celdasTabla4,valores5);
})
