$(document).ready(function() {
    // Submit login form
    $(document).on('submit', '#login-form', function(event) {
        event.preventDefault();

        var email = $('#email').val();
        var password = $('#password').val();
        var emailError = '';
        var passwordError = '';

        $('#email-error').remove();
        $('#password-error').remove();

        if (!email) {
            emailError = 'Email is required.';
        } else if (!validateEmail(email)) {
            emailError = 'Invalid email format.';
        }

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
            data: $.param({ username: email, password: password }),
            success: function(response) {
                if (response.access_token) {
                    console.log("Access token received:", response.access_token); // Debugging line
                    localStorage.setItem('accessToken', response.access_token);
                    localStorage2.setItem('role', response.role)

                    var token = parseJwt(response.access_token);
                    var role = token.role;

                    switch (role) {
                        case 'blood-bank-admin':
                            console.log(role)
                            window.location.href = '/bloodbank/dashboard';
                            break;
                        case 'hospital-admin':
                            console.log(role)
                            window.location.href = '/cairo_hospital/dashboard';
                            break;
                        default:
                            console.log(role)
                            window.location.href = '/';
                            break;
                    }
                } else {
                    $('#error-message').addClass('show').text('Invalid credentials');
                }
            },
            error: function() {
                $('#error-message').addClass('show').text('Invalid credentials');
            }
        });
    });

    // Input field event handler
    $(document).on('input', '#email, #password', function() {
        $('#error-message').removeClass('show');
        $('#email-error').remove();
        $('#password-error').remove();
    });

    // Validate email format
    function validateEmail(email) {
        var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Parse JWT token
    function parseJwt(token) {
        var base64Url = token.split('.')[1];
        var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));

        return JSON.parse(jsonPayload);
    }

    // Global AJAX setup to include Authorization header
    $.ajaxSetup({
        beforeSend: function(xhr) {
            var token = localStorage.getItem('accessToken');
            if (token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
            }
        }
    });
});
