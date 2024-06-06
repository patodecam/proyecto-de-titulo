document.addEventListener('DOMContentLoaded', function () {
    var dropdowns = document.querySelectorAll('.dropdown');
    
    dropdowns.forEach(function (dropdown) {
        var dropdownToggle = dropdown.querySelector('.dropdown-toggle');
        var dropdownMenu = dropdown.querySelector('.dropdown-menu');
        
        dropdownToggle.addEventListener('click', function (event) {
            event.preventDefault();
            var isOpen = dropdown.classList.contains('show');
            
            // Close all dropdowns
            document.querySelectorAll('.dropdown').forEach(function (otherDropdown) {
                otherDropdown.classList.remove('show');
                otherDropdown.querySelector('.dropdown-menu').classList.remove('show');
            });
            
            // Toggle the current dropdown
            if (!isOpen) {
                dropdown.classList.add('show');
                dropdownMenu.classList.add('show');
            }
        });
        
        // Hide dropdown when clicking outside
        document.addEventListener('click', function (event) {
            if (!dropdown.contains(event.target)) {
                dropdown.classList.remove('show');
                dropdownMenu.classList.remove('show');
            }
        });
    });
});
