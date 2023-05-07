(function(){

    const btneliminar=document.querySelectorAll(".btneliminar");
btneliminar.forEach(btn=> {
    btn.addEventListener('click',(e) =>{
        const confirmacion=confirm('¿Esta seguro de eliminar este item?')
        if(!confirmacion){
            e.preventDefault();
        }
    });
});
})();