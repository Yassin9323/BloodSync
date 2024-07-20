import { setupAjax, initializeRouteHandling } from './utils.js';
$(document).ready(function() {

    setupAjax();
    const authority = initializeRouteHandling();

    // Function to access the blood bank inventory endpoint
    function getInventory() {
        // console.log(authority)
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
