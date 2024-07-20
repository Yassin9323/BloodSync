document.getElementById('register-form').addEventListener('submit', function(event) {
    // Prevent form submission
    event.preventDefault();

    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(function(error) {
        error.style.display = 'none';
    });
    // function showAdditionalOptions() {
    //     var roleSelect = document.getElementById("role");
    //     var hospitalNames = document.getElementById("hospitalNames");

    //     if (roleSelect.value === "hospital-admin") {
    //         hospitalNames.classList.remove("hidden");
    //     } else {
    //         hospitalNames.classList.add("hidden");
    //     }
    // }
    // showAdditionalOptions()
    // Flag to check if the form is valid
    let isValid = true;

    // Validate username
    const username = document.getElementById('username');
    if (!username.value.trim()) {
        document.getElementById('usernameError').style.display = 'block';
        isValid = false;
    }

    // Validate email
    const email = document.getElementById('email');
    if (!email.value.trim() || !validateEmail(email.value)) {
        document.getElementById('emailError').style.display = 'block';
        isValid = false;
    }

    // Validate role
    const role = document.getElementById('role');
    if (!role.value) {
        document.getElementById('roleError').style.display = 'block';
        isValid = false;
    }

    const place_name = document.getElementById('place_name');
    if (!place_name.value) {
        document.getElementById('placeError').style.display = 'block';
        isValid = false;
    }

    // Validate password
    const password = document.getElementById('password');
    if (!password.value.trim()) {
        document.getElementById('passwordError').style.display = 'block';
        isValid = false;
    }

    // If the form is valid, submit it
    if (isValid) {
        this.submit();
    }
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
