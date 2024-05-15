$(document).ready(function(){
    $("#datepicker").datepicker({
        dateFormat: "yy-mm-dd",
        beforeShowDay: function(date) {
            var string = jQuery.datepicker.formatDate('yy-mm-dd', date);
            return [ availableDates.indexOf(string) != -1 ]
        }
    });
});

const availableDates = ["2024-05-20", "2024-05-21", "2024-05-22"]; // Sample dates for demonstration