//Boton de menu

const nav  = document.querySelector("nav");
const abrir  = document.getElementById("abrir");
const cerrar  = document.getElementById("cerrar");


abrir.addEventListener("click", () => {
    nav.classList.add("nav_visible");
    console.log("hola")
})

cerrar.addEventListener("click", () => {
    nav.classList.remove("nav_visible");
})
