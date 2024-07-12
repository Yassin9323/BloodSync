document.getElementById('login-form').addEventListener('submit', function(event) {
    // Prevent form submission
    event.preventDefault();

    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(function(error) {
        error.style.display = 'none';
    });

    // Flag to check if the form is valid
    let isValid = true;

    // Validate email
    const email = document.getElementById('email');
    if (!email.value.trim() || !validateEmail(email.value)) {
        document.getElementById('emailError').style.display = 'block';
        isValid = false;
    }



//    Validate password
   const password = document.getElementById('password');
   if (!password.value.trim()) {
       document.getElementById('passwordError').style.display = 'block';
       isValid = false;
   }


    // If the form is valid, submit it
    if (isValid) {
        event.target.submit();
    }
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
