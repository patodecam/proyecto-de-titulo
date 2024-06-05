document.addEventListener('DOMContentLoaded', function() {
    const formularioReserva = document.getElementById('formularioReserva');
    const cantidadPersonas = document.getElementById('cantidad_personas');
    const fecha = document.getElementById('fecha');
    const aceptarTerminos = document.getElementById('aceptar_terminos');
    const errorCantidadPersonas = document.getElementById('errorCantidadPersonas');
    const errorFecha = document.getElementById('errorFecha');
    const errorTerminosCondiciones = document.getElementById('errorTerminosCondiciones');

    formularioReserva.addEventListener('submit', function(evento) {
        let valido = true;

        errorCantidadPersonas.textContent = '';
        errorFecha.textContent = '';
        errorTerminosCondiciones.textContent = '';

        
        const cantidadValue = cantidadPersonas.value.trim();
        if (cantidadValue === '' || isNaN(cantidadValue) || cantidadValue < 30 || cantidadValue > 200) {
            errorCantidadPersonas.textContent = 'La cantidad de personas debe estar entre 30 y 200.';
            valido = false;
        }

       
        const fechaValue = fecha.value.trim();
        if (fechaValue === '') {
            errorFecha.textContent = 'La fecha de reserva es obligatoria.';
            valido = false;
        } else {
            const hoy = new Date();
            const seleccionada = new Date(fechaValue);
            const cincoDiasEnElFuturo = new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate() + 5);
            if (seleccionada <= hoy) {
                errorFecha.textContent = 'La fecha de reserva no puede ser una fecha pasada.';
                valido = false;
            } else if (seleccionada <= cincoDiasEnElFuturo) {
                errorFecha.textContent = 'La fecha de reserva debe ser al menos con 5 dias de anticipación.';
                valido = false;
            }
        }

        
        if (!aceptarTerminos.checked) {
            errorTerminosCondiciones.textContent = 'Debe aceptar los términos y condiciones.';
            valido = false;
        }

        if (!valido) {
            evento.preventDefault(); 
        }

    });

    
    cantidadPersonas.addEventListener('input', function() {
        errorCantidadPersonas.textContent = '';
    });

    fecha.addEventListener('input', function() {
        errorFecha.textContent = '';
    });

    aceptarTerminos.addEventListener('change', function() {
        errorTerminosCondiciones.textContent = '';
    });
});