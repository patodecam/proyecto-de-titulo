// Evento menu desplegable
document.addEventListener('DOMContentLoaded', function () {
    var dropdown = document.querySelector('.dropdown');
    var dropdownMenu = document.querySelector('.dropdown-menu');

    dropdownMenu.addEventListener('show.bs.dropdown', function () {
        dropdown.classList.add('open');
    });

    dropdownMenu.addEventListener('hide.bs.dropdown', function () {
        dropdown.classList.remove('open');
    });
});
