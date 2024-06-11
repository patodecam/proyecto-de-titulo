$(document).ready(function() {
    // Efecto de animación al cargar la página
    $('main.container').hide().fadeIn(1000);

    // Validación del formulario
    $('form').submit(function(event) {
        var comentario = $('#id_comentario').val();
        var escalaServicio = $('#id_escala_servicio').val();

        if (!comentario || !escalaServicio) {
            alert('Por favor, completa todos los campos.');
            event.preventDefault();
        } else if (escalaServicio < 1 || escalaServicio > 5) {
            alert('Por favor, ingresa una escala de servicio válida (1-5).');
            event.preventDefault();
        }
    });

    // Protección de enlaces en los comentarios (simple escape)
    $('.lista-referencias li').each(function() {
        var comentario = $(this).find('em').text();
        var sanitizedComentario = comentario.replace(/</g, "&lt;").replace(/>/g, "&gt;");
        $(this).find('em').text(sanitizedComentario);
    });
});
