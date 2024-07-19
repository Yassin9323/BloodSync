$(document).ready(function() {
    // Global AJAX setup to include Authorization header
    $.ajaxSetup({
        beforeSend: function(xhr) {
            var token = localStorage.getItem('accessToken');
            var role = localStorage2.getItem('role')
            if (token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
            }
        }
    });
    const route = window.location.pathname.replace('/', '');
    route_list = route.split("/");
    if (route_list[0] === "bloodbank" && role === "blood-bank-admin") {
        authority = route_list[0]

    } if (route_list[0] === "bloodbank" && role === "hospital-admin") {
            console.error(`Not Authorized:`);

    } if (route_list[0] != "bloodbank" ) {
        x = route_list[0].split("_")
    }

    
    // Function to access the blood bank inventory endpoint
    function getInventory() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/dashboard/inventory`,
            type: 'GET',
            success: function(response) {
                console.log(`${authority} inventory data:`, response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} inventory:`, status, error);
                // Handle the error
            }
        });
    }

    // Function to access the blood bank units endpoint
    function getInventory_total_units() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/dashboard/inventory_total_units`,
            type: 'GET',
            success: function(response) {
                console.log(`${authority} units data:`, response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} units data:`, status, error);
                // Handle the error
            }
        });
    }

    // Function to access the blood bank requests endpoint
    function getRequests() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/dashboard/requests`,
            type: 'GET',
            success: function(response) {
                console.log(`${authority} requests data:`, response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} requests:`, status, error);
                // Handle the error
            }
        });
    }

    // Function to access the blood bank transactions endpoint
    function getTransactions() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/dashboard/transactions`,
            type: 'GET',
            success: function(response) {
                console.log(`${authority} transactions data:`, response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} transactions:`, status, error);
                // Handle the error
            }
        });
    }

    // Calling the functions to connect endpoints
    getInventory();
    getInventory_total_units();
    getRequests();
    getTransactions();
});
