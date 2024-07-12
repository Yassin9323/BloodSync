$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way
        var email = $('#email').val();
        var password = $('#password').val();
        
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {email: email, password: password},
            success: function(response) {
                window.location.href = '/dashboard';
            },
            error: function(response) {
                window.location.href = '/error';
            }
        });
    });

    // $('h1').hide();

});
