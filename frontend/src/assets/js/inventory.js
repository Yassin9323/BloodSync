$(document).ready(function() {
    // Global AJAX setup to include Authorization header
    $.ajaxSetup({
        beforeSend: function(xhr) {
            var token = localStorage.getItem('accessToken');
            if (token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
            }
        }
    });

    // Function to access the Bloodbank_inventory endpoint
    function getBloodbank_inventory() {
        $.ajax({
            url: 'http://127.0.0.1:8000/bloodbank/inventory/',
            type: 'GET',
            success: function(response) {
                console.log("Bloodbank inventory data:", response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error("Error accessing bloodbank inventory:", status, error);
                // Handle the error
            }
        });
    }

    // Function to access the Hospital_inventory endpoint
    function getHospital_inventory() {
        var hospitalName = "cairo"
        $.ajax({
            url: `http://127.0.0.1:8000/bloodbank/inventory/${hospitalName}_inventory`,
            type: 'GET',
            success: function(response) {
                console.log("hospital inventory data:", response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error("Error accessing hospital inventory:", status, error);
                // Handle the error
            }
        });
    }

    // Call the function to access the endpoint
    getBloodbank_inventory();
    getHospital_inventory();
});
