import { setupAjax, initializeRouteHandling } from './utils.js';
$(document).ready(function() {

    setupAjax();
    const authority = initializeRouteHandling();

    // Function to access the Bloodbank_inventory endpoint
    function getPending_requests() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/requests/pending`,
            type: `GET`,
            success: function(response) {
                console.log(`${authority} pending requests :`, response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} pending requests:`, status, error);
                // Handle the error
            }
        });
    }

    // Function to access the Bloodbank_inventory endpoint
    function getTotal_requests() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/requests/total`,
            type: `GET`,
            success: function(response) {
                console.log(`${authority} total requests :`, response);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} total requests:`, status, error);
                // Handle the error
            }
        });
    }


    function updateRequest_status() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/requests/update_status`,
            type: `PUT`,
            success: function(response) {
                console.log(`Updting Status`);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                if(authority === "bloodbank"){
                    console.error(`Error accessing Updting Status:`);
                }
            }
        });
    }

    function create_request() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/requests/create_request`,
            type: `POST`,
            success: function(response) {
                console.log(`Updting Status`);
                // Handle the response data
            },
            error: function(xhr, status, error) {
                if (authority !== "bloodbank"){
                    console.error(`Error can't create request:`);
                }
                // Handle the error
            }
        });
    }
    // Call the function to access the endpoint
    getPending_requests();
    getTotal_requests();
    updateRequest_status();
    create_request();

});
