function botonesCrearCuenta(){
    if(document.contains(document.getElementById("bienvenido-boton-escondido"))){
        document.getElementById("bienvenido-boton-escondido").setAttribute("id","bienvenido-boton-mostrado");
    }else{
        document.getElementById("bienvenido-boton-mostrado").setAttribute("id","bienvenido-boton-escondido");
    }  
}

function botonAlLogin(){
    if(document.contains(document.getElementById("login-escondido"))){
        document.getElementById("login-escondido").setAttribute("id","login-mostrado");
    }else{
        document.getElementById("login-mostrado").setAttribute("id","login-escondido");
    } 
}

function confirmarBorrarUsuario(){
    var d = document.getElementById("confirmar-borrar-usuario");
    if(d.style.display=="none"){
        d.style.display="block";
    }else{
        d.style.display="none";
    }
}