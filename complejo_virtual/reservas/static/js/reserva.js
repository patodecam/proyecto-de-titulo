document.addEventListener('DOMContentLoaded', () => {
    const btnReservar = document.getElementById('btn-reservar');

    btnReservar.addEventListener('click', (evento) => {
        btnReservar.classList.add('btn-clicked');
        setTimeout(() => {
            btnReservar.classList.remove('btn-clicked');
        }, 300);
    });

    const formularioReserva = document.getElementById('formularioReserva');
    const cantidadPersonas = document.getElementById('cantidad_personas');
    const fecha = document.getElementById('fecha');
    const aceptarTerminos = document.getElementById('aceptar_terminos');
    const errores = {
        cantidad: document.getElementById('errorCantidadPersonas'),
        fecha: document.getElementById('errorFecha'),
        terminos: document.getElementById('errorTerminosCondiciones')
    };

    const limpiarErrores = () => {
        Object.values(errores).forEach(error => error.textContent = '');
    };

    const mostrarError = (elemento, mensaje) => {
        elemento.textContent = mensaje;
    };

    formularioReserva.addEventListener('submit', (evento) => {
        limpiarErrores();
        let valido = true;

        const cantidadValue = cantidadPersonas.value.trim();
        if (!cantidadValue || isNaN(cantidadValue) || cantidadValue < 30 || cantidadValue > 200) {
            mostrarError(errores.cantidad, 'La cantidad de personas debe estar entre 30 y 200.');
            valido = false;
        }

        const fechaValue = fecha.value.trim();
        if (!fechaValue) {
            mostrarError(errores.fecha, 'La fecha de reserva es obligatoria.');
            valido = false;
        } else {
            const hoy = new Date();
            const seleccionada = new Date(fechaValue);
            const cincoDiasEnElFuturo = new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate() + 5);
            if (seleccionada <= hoy) {
                mostrarError(errores.fecha, 'La fecha de reserva no puede ser una fecha pasada.');
                valido = false;
            } else if (seleccionada <= cincoDiasEnElFuturo) {
                mostrarError(errores.fecha, 'La fecha de reserva debe ser al menos con 5 días de anticipación.');
                valido = false;
            }
        }

        if (!aceptarTerminos.checked) {
            mostrarError(errores.terminos, 'Debe aceptar los términos y condiciones.');
            valido = false;
        }

        if (!valido) {
            evento.preventDefault();
        }
    });

    cantidadPersonas.addEventListener('input', () => errores.cantidad.textContent = '');
    fecha.addEventListener('input', () => errores.fecha.textContent = '');
    aceptarTerminos.addEventListener('change', () => errores.terminos.textContent = '');
});
