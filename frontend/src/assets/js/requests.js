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
    function getPending_requests() {
        $.ajax({
            url: 'http://127.0.0.1:8000/bloodbank/requests/pending',
            type: 'GET',
            success: function(response) {
                console.log("Bloodbank pending requests :", response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error("Error accessing bloodbank pending requests:", status, error);
                // Handle the error
            }
        });
    }

    // Function to access the Bloodbank_inventory endpoint
    function getTotal_requests() {
        $.ajax({
            url: 'http://127.0.0.1:8000/bloodbank/requests/total',
            type: 'GET',
            success: function(response) {
                console.log("Bloodbank total requests :", response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error("Error accessing bloodbank total requests:", status, error);
                // Handle the error
            }
        });
    }


    // Function to access the Hospital_inventory endpoint
    function updateRequest_status() {
        var hospitalName = "cairo"
        $.ajax({
            url: `http://127.0.0.1:8000/bloodbank/requests/update_status`,
            type: 'PUT',
            success: function(response) {
                console.log("Updting Status");
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error("Error accessing Updting Status:");
                // Handle the error
            }
        });
    }
    // Call the function to access the endpoint
    getPending_requests();
    getTotal_requests();
    updateRequest_status();

});
