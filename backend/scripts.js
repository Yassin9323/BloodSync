$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way
        var username = $('#email').val();
        var password = $('#password').val();
        
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {email: email, password: password},
            success: function(response) {
                $('#login-result').html('<p>' + response.message + '</p>');
            },
            error: function(response) {
                $('#login-result').html('<p>' + response.responseJSON.detail + '</p>');
            }
        });
    });

    // $('h1').hide();

});
