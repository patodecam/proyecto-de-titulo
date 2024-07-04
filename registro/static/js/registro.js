document.addEventListener('DOMContentLoaded', function(){
    const fields = [
        'primerNombre', 'segundoNombre', 'primerApellido', 'segundoApellido',
        'rut', 'dv', 'correo', 'password1', 'password2', 'terminosCondiciones'
    ];
    
    const formulario = document.getElementById('formularioRegistro');

    formulario.addEventListener('submit', function(evento){
        let valid = true;
        
        fields.forEach(field => {
            const input = document.getElementById(field);
            const errorMessage = document.getElementById(`error${capitalize(field)}`);
            if (!input.checkValidity()) {
                valid = false;
                errorMessage.textContent = input.validationMessage;
            } else {
                errorMessage.textContent = '';
            }
        });

        if (document.getElementById('password1').value !== document.getElementById('password2').value) {
            valid = false;
            document.getElementById('errorPassword2').textContent = 'Las contraseñas no coinciden.';
        }

        if (!valid) {
            evento.preventDefault();
        }
    });

    fields.forEach(field => {
        const input = document.getElementById(field);
        input.addEventListener('input', () => {
            const errorMessage = document.getElementById(`error${capitalize(field)}`);
            if (input.checkValidity()) {
                errorMessage.textContent = '';
            }
        });
    });

    function capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
});
