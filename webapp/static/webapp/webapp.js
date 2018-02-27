$( document ).ready(function() {
    $.get( api_url, function( data ) {
        $( ".result" ).html( data );
        alert(data);
    });
});