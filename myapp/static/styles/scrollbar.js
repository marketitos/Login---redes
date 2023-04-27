//Boton de menu

const scrollbar  = document.getElementById("scrollbar");
const abrir  = document.getElementById("abrir");
const cerrar  = document.getElementById("cerrar");


abrir.addEventListener("click", () => {
    scrollbar.classList.add("nav_visible");
    console.log("hola")
})

cerrar.addEventListener("click", () => {
    scrollbar.classList.remove("nav_visible");
})
