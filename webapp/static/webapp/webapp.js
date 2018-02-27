$( document ).ready(function() {
    alert('js loaded');
    $.get( api_url, function( data ) {
        $( ".result" ).html( data );
        alert(data);
    });
});