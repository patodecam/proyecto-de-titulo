document.addEventListener('DOMContentLoaded', function() {
    const formularioLogin = document.getElementById('formularioLogin');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const errorCorreo = document.getElementById('errorCorreo');
    const errorPassword = document.getElementById('errorPassword');

    const alertDiv = document.querySelector('.alert');
    if (alertDiv) {
        setTimeout(() => {
            alertDiv.style.display = 'none';
        }, 3000);
    }

    formularioLogin.addEventListener('submit', function(event) {
        let valid = true;

        
        errorCorreo.textContent = '';
        errorPassword.textContent = '';

        
        const emailValue = emailInput.value.trim();
        if (emailValue === '') {
            errorCorreo.textContent = 'El correo electrónico es obligatorio.';
            valid = false;
        } else if (!emailValue.includes('@')) {
            errorCorreo.textContent = 'Ingrese un formato correcto de correo electornico.';
            valid = false;
        } else if (!validateEmail(emailValue)) {
            errorCorreo.textContent = 'Por favor, ingrese un correo electrónico válido.';
            valid = false;
        }

        
        const passwordValue = passwordInput.value.trim();
        if (passwordValue === '') {
            errorPassword.textContent = 'La contraseña es obligatoria.';
            valid = false;
        }

        if (!valid) {
            event.preventDefault();
        }
    });

    
    emailInput.addEventListener('input', function() {
        errorCorreo.textContent = '';
    });

    passwordInput.addEventListener('input', function() {
        errorPassword.textContent = '';
    });

    function validateEmail(email) {
        
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
