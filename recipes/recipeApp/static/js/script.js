$(document).ready(function() {
    document.getElementById("datePicker").max = new Date().toISOString().split("T")[0];


    // $('[type="date"].max-today').prop('datePicker', function(){
    //     return new Date().toJSON().split('T')[0];
    // });

});