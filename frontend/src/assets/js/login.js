$(document).ready(function() {
    $(document).on('submit', '#login-form', function(event) {
        event.preventDefault();

        var email = $('#email').val();
        var password = $('#password').val();
        var emailError = '';
        var passwordError = '';

        // Clear previous error messages
        $('#email-error').remove();
        $('#password-error').remove();

        // Validate email
        if (!email) {
            emailError = 'Email is required.';
        } else if (!validateEmail(email)) {
            emailError = 'Invalid email format.';
        }

        // Validate password
        if (!password) {
            passwordError = 'Password is required.';
        }

        if (emailError || passwordError) {
            if (emailError) {
                $('<div id="email-error" class="error-message">' + emailError + '</div>').insertAfter('#email');
            }
            if (passwordError) {
                $('<div id="password-error" class="error-message">' + passwordError + '</div>').insertAfter('#password');
            }
            return;
        }

        $.ajax({
            url: '/login',
            type: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: $.param({ email: email, password: password }),
            success: function(response) {
                if (response.success) {
                    console.log("Login successful, redirecting to dashboard...");
                    window.location.href = '/dashboard';
                } else {
                    // Show error message if login fails
                    console.log("Login failed, showing error message.");
                    $('#error-message').addClass('show').text('Invalid credentials');
                }
            },
            error: function() {
                // Show error message on AJAX error
                $('#error-message').addClass('show').text('Invalid credentials');
            }
        });
    });

    $(document).on('input', '#email, #password', function() {
        console.log('Input event triggered');
        $('#error-message').removeClass('show');
        $('#email-error').remove();
        $('#password-error').remove();
    });

    function validateEmail(email) {
        var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
