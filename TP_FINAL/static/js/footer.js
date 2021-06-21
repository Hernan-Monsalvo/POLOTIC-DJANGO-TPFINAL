
/*------------- Cambiar texto Copyright -----------*/

function cambiarTextoCR() {    
    var width = document.documentElement.clientWidth;   /*mide ancho de la pantalla*/
    
    if (width > 410){
        document.getElementById("copyright").innerHTML = "JAGUARETE KAA S.A. Copyright © 2021 - Hernan Monsalvo. Todos los derechos reservados";
 
    }else{
        document.getElementById("copyright").innerHTML = "J.K.S.A. ©2021-Todos los derechos reservados.";
    }
}

cambiarTextoCR();

window.addEventListener("resize", cambiarTextoCR); /*evento que se ejecuta cuando se hace un cambio de tamaño en la pagina*/

