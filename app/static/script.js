function botonesCrearCuenta(){
    if(document.contains(document.getElementById("welcome-hidden-button"))){
        document.getElementById("welcome-hidden-button").setAttribute("id","welcome-show-button");
    }else{
        document.getElementById("welcome-show-button").setAttribute("id","welcome-hidden-button");
    }  
}

function botonAlLogin(){
    if(document.contains(document.getElementById("login-hidden"))){
        document.getElementById("login-hidden").setAttribute("id","login-show");
    }else{
        document.getElementById("login-show").setAttribute("id","login-hidden");
    } 
}