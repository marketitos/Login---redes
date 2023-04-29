//Boton de menu

const barritas = document.querySelector('.cerrar_menu');

barritas.addEventListener('click', function(){
    document.getElementById('sidebar').classList.toggle('active');
})
