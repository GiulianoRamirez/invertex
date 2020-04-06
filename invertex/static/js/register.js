$(document).ready(function() {
    console.log("ready!");

    $(function() {
        $("#datepicker").datepicker({
            autoclose: true,
            todayHighlight: true
        }).datepicker('update', new Date());
        $('#abc').val("Fecha nacimiento");
    });





});