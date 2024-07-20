import { setupAjax, initializeRouteHandling } from './utils.js';
$(document).ready(function() {

    setupAjax();
    const authority = initializeRouteHandling();
    
    // Function to access the Bloodbank_inventory endpoint
    function get_inventory() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/inventory/`,
            type: 'GET',
            success: function(response) {
                console.log(`${authority} inventory:`, response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} inventory:`, status, error);
                // Handle the error
            }
        });
    }

    // Function to access the Hospital_inventory endpoint
    function getHospital_inventory() {
        var hospitalName = "cairo" // it will take the value from html ID to be dynamic based on user's selection
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/inventory/${hospitalName}_inventory`,
            type: 'GET',
            success: function(response) {
                console.log("hospital inventory data:", response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                if (authority === "bloodbank"){
                    console.error("Error accessing hospital inventory:", status, error);
                }                
            }
        });
    }

    // Call the function to access the endpoint
    get_inventory();
    getHospital_inventory();
});
