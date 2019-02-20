function rechazar(e){
    $("#id1").val(e.id);
    $("#approb").val("rechazado")
    $('#formulario').submit();
}

function aprobar(e){
    $("#id1").val(e.id);
    $("#approb").val("aprobado")
    $('#formulario').submit();
}