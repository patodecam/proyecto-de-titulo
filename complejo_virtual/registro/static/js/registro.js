document.addEventListener('DOMContentLoaded', function(){
    const primerNombre = document.getElementById('primerNombre');
    const segundoNombre = document.getElementById('segundoNombre');
    const primerApellido = document.getElementById('primerApellido');
    const segundoApellido = document.getElementById('segundoApellido');
    const rut = document.getElementById('rut');
    const dv = document.getElementById('dv');
    const correo = document.getElementById('correo');
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');
    const terminosCondiciones = document.getElementById('terminosCondiciones');

    const formulario=document.getElementById('formularioRegistro');

    formulario.addEventListener('submit',function(evento){
        let valid = true;

        if (!/^[a-zA-Z]+(?: [a-zA-Z]+)*$/.test(primerNombre.value.trim())) {
            showError('errorPrimerNombre', 'El nombre solo debe contener letras y un espacio entre palabras.');
            valid = false;
        } else {
            clearError('errorPrimerNombre');
        }

        if (segundoNombre.value.trim() && !/^[a-zA-Z]+(?: [a-zA-Z]+)*$/.test(segundoNombre.value.trim())) {
            showError('errorSegundoNombre', 'El nombre solo debe contener letras y un espacio entre palabras.');
            valid = false;
        } else {
            clearError('errorSegundoNombre');
        }

        if (!/^[a-zA-Z]+(?: [a-zA-Z]+)*$/.test(primerApellido.value.trim())) {
            showError('errorPrimerApellido', 'El apellido solo debe contener letras y un espacio entre palabras.');
            valid = false;
        } else {
            clearError('errorPrimerApellido');
        }

        if (segundoApellido.value.trim() && !/^[a-zA-Z]+(?: [a-zA-Z]+)*$/.test(segundoApellido.value.trim())) {
            showError('errorSegundoApellido', 'El apellido solo debe contener letras y un espacio entre palabras.');
            valid = false;
        } else {
            clearError('errorSegundoApellido');
        }

        if (!/^\d{8}$/.test(rut.value.trim())) {
            showError('errorRut', 'El RUT debe contener exactamente 8 dígitos.');
            valid = false;
        } else {
            clearError('errorRut');
        }

        if (!/^[0-9Kk]$/.test(dv.value.trim())) {
            showError('errorDv', 'El DV debe ser un número entre 0 y 9 o la letra K.');
            valid = false;
        }else {
            clearError('errorDv');
        }

        if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(correo.value.trim())) {
            showError('errorCorreo', 'El formato del correo no es válido.');
            valid = false;
        } else {
            clearError('errorCorreo');
        }

        if (!/^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9]).{8,}$/.test(password1.value.trim())) {
            showError('errorPassword1', 'La contraseña debe tener al menos 8 caracteres, una letra mayúscula, un número y un carácter especial.');
            valid = false;
        } else {
            clearError('errorPassword1');
        }

        if (password1.value.trim() !== password2.value.trim()) {
            showError('errorPassword2', 'Las contraseñas no coinciden.');
            valid = false;
        } else {
            clearError('errorPassword2');
        }

        if (!terminosCondiciones.checked) {
            showError('errorTerminosCondiciones', 'Debe aceptar los términos y condiciones.');
            valid = false;
        } else {
            clearError('errorTerminosCondiciones');
        }



        
        if (!valid) {
            evento.preventDefault(); // Evitar el envío del formulario si hay errores
        }




    });

    function showError(elementId, message) {
        const errorElement = document.getElementById(elementId);
        errorElement.textContent = message;
        errorElement.style.color = '#FF6500';
    }

    function clearError(elementId) {
        const errorElement = document.getElementById(elementId);
        errorElement.textContent = '';
    }

    


    primerNombre.addEventListener('input', function() {
        if (!/^[a-zA-Z]+(?: [a-zA-Z]+)*$/.test(primerNombre.value.trim())) {
            showError('errorPrimerNombre', 'El nombre solo debe contener letras y un espacio entre palabras.');
        } else {
            clearError('errorPrimerNombre');
        }
    });

    segundoNombre.addEventListener('input', function() {
        if (segundoNombre.value.trim() && !/^[a-zA-Z]+(?: [a-zA-Z]+)*$/.test(segundoNombre.value.trim())) {
            showError('errorSegundoNombre', 'El nombre solo debe contener letras y un espacio entre palabras.');
        } else {
            clearError('errorSegundoNombre');
        }
    });

    primerApellido.addEventListener('input', function() {
        if (!/^[a-zA-Z]+(?: [a-zA-Z]+)*$/.test(primerApellido.value.trim())) {
            showError('errorPrimerApellido', 'El apellido solo debe contener letras y un espacio entre palabras.');
        } else {
            clearError('errorPrimerApellido');
        }
    });

    segundoApellido.addEventListener('input', function() {
        if (segundoApellido.value.trim() && !/^[a-zA-Z]+(?: [a-zA-Z]+)*$/.test(segundoApellido.value.trim())) {
            showError('errorSegundoApellido', 'El apellido solo debe contener letras y un espacio entre palabras.');
        } else {
            clearError('errorSegundoApellido');
        }
    });

    rut.addEventListener('input', function() {
        if (!/^\d{8}$/.test(rut.value.trim())) {
            showError('errorRut', 'El RUT debe contener exactamente 8 dígitos.');
        } else {
            clearError('errorRut');
        }
    });

    dv.addEventListener('input', function() {
        if (!/^[0-9Kk]$/.test(dv.value.trim())) {
            showError('errorDv', 'El DV debe ser un número entre 0 y 9 o la letra K.');
        } else {
            clearError('errorDv');
        }
    });

    correo.addEventListener('input', function () {
        if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(correo.value.trim())) {
            showError('errorCorreo', 'El formato del correo no es válido.');
        } else {
            clearError('errorCorreo');
        }
    });

    password1.addEventListener('input', function () {
        if (!/^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9]).{8,}$/.test(password1.value.trim())) {
            showError('errorPassword1', 'La contraseña debe tener al menos 8 caracteres, una letra mayúscula, un número y un carácter especial.');
        } else {
            clearError('errorPassword1');
        }
    });

    password2.addEventListener('input', function () {
        if (password1.value.trim() !== password2.value.trim()) {
            showError('errorPassword2', 'Las contraseñas no coinciden.');
        } else {
            clearError('errorPassword2');
        }
    });

    terminosCondiciones.addEventListener('change', function () {
        if (!terminosCondiciones.checked) {
            showError('errorTerminosCondiciones', 'Debe aceptar los términos y condiciones.');
        } else {
            clearError('errorTerminosCondiciones');
        }
    });
});
