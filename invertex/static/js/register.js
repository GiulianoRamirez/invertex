$(document).ready(function() {

    if (localStorage.getItem('nombres') != null) {
        window.location.href = "/main/";
    }

    hidden_logeada_o_no()
    console.log("ready register!");



    $(function() {
        $("#datepicker").datepicker({
            autoclose: true,
            todayHighlight: true
        }).datepicker('update', new Date());
        $('#abc').val("Fecha nacimiento");
    });

    $(function() {
        $('#rut').Rut({
            validation: false,
            format_on: 'keyup',
            digito_verificador: '#digitoVerificador'
        });
    });



    var password = document.getElementById("contrasena"),
        confirm_password = document.getElementById("repetirContrasena");

    function validatePassword() {
        if (password.value != confirm_password.value) {
            confirm_password.setCustomValidity("Las contraseñas no son iguales");
        } else {
            confirm_password.setCustomValidity('');
        }
    }

    password.onchange = validatePassword;
    confirm_password.onkeyup = validatePassword;



});