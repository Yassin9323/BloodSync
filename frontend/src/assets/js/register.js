$(document).ready(function() {
    // Submit registration form
    $(document).on('submit', '#register-form', function(event) {
        event.preventDefault();

        // Clear previous error messages
        $('.error-message').hide();

        // Flag to check if the form is valid
        let isValid = true;

        // Validate username
        const username = $('#username').val();
        if (!username.trim()) {
            $('#usernameError').show();
            isValid = false;
        }

        // Validate email
        const email = $('#email').val();
        if (!email.trim() || !validateEmail(email)) {
            $('#emailError').show();
            isValid = false;
        }

        // Validate role
        const role = $('#role').val();
        if (!role) {
            $('#roleError').show();
            isValid = false;
        }

        // Validate place_name
        const place_name = $('#place_name').val();
        if (!place_name) {
            $('#placeError').show();
            isValid = false;
        }

        // Validate password
        const password = $('#password').val();
        if (!password.trim()) {
            $('#passwordError').show();
            isValid = false;
        }

        // If the form is valid, submit it
        if (isValid) {
            const formData = {
                email: email,
                username: username,
                password: password,
                role: role,
                place_name: place_name
            };

            $.ajax({
                url: '/register',
                type: 'POST',
                contentType: 'application/x-www-form-urlencoded',
                data: $.param(formData),
                success: function(response) {
                    // Save the token to localStorage or any other storage
                    localStorage.setItem('accessToken', response.access_token);

                    // Parse the JWT token
                    var token = parseJwt(response.access_token);
                    var role = token.role;
                    var place_name = token.place_name;
                    if (place_name) { // Ensure place_name is not null
                        place_name = place_name.replace('-', '_').toLowerCase();
                    }
                    console.log(place_name)
                    localStorage.setItem('role', role)
                    localStorage.setItem('place_name', place_name)
                    switch (role) {
                        case 'blood-bank-admin':
                            console.log(role)
                            window.location.href = '/bloodbank/dashboard';
                            break;
                        case 'hospital-admin':
                            // console.log(role)
                            window.location.href = `/${place_name}/dashboard`;
                            break;
                        default:
                            // console.log(role)
                            window.location.href = '/';
                            break;
                    }
                },
                error: function(xhr) {
                    const errorResponse = xhr.responseJSON;
                    if (errorResponse && errorResponse.detail) {
                        alert(errorResponse.detail);
                    } else {
                        alert('An error occurred during registration.');
                    }
                }
            });
        }
    });

    // Validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Parse JWT token
    function parseJwt(token) {
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));

        return JSON.parse(jsonPayload);
    }
});