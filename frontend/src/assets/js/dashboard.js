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

                const tbody = $('.inventory-card table tbody');
                tbody.empty(); // Clear existing table rows
                const data = response.inventory

                data.forEach(item => {
                    const row = `<tr>
                        <td>${item.blood_type}</td>
                        <td>${item.available_units}</td>
                    </tr>`;
                    tbody.append(row);
                });
                console.log(data)
        
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

                const num = $('#total_units');
                num.empty(); // Clear existing table rows
                const data = response.total_units;
                const p = `<p> ${data} </p>`;
                num.append(p);
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

                const pending = $('#pending');
                pending.empty(); // Clear existing table rows
                const pData = response.requests.pending;
                const p1 = `<p> ${pData} </p>`;
                pending.append(p1);

                const total = $('#total');
                total.empty(); // Clear existing table rows
                const tData = response.requests.total;
                const p2 = `<p> ${tData} </p>`;
                total.append(p2);

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

                const transaction = $('.history-table table tbody');
                transaction.empty(); // Clear existing table rows
                const data = response.latest_transactions;

                data.forEach(item => {
                    const row = `<tr>
                        <td>${item.hospital_name}</td>
                        <td>${item.blood_type}</td>
                        <td>${item.units}</td>
                        <td>${item.req_num}</td>
                    </tr>`;
                    transaction.append(row);
                    console.log(item.hospital_name)
                });
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} transactions:`, status, error);
                // Handle the error
            }
        });
    }

    function url() {
        $("#inventory_page").click(function(event){
            event.preventDefault();
            $.ajax({
                url: "/inventory",  // URL of the FastAPI endpoint
                type: "GET",
                success: function(response){
                    // Do something with the response
                    var link = response.new_url
                    var link = link.replace('x', `${authority}`);
                    console.log(link)
                    window.location.href =`http://127.0.0.1:8000${link}`                    // Redirect to the new URL
                },
                error: function(error){
                    console.log("Error:", error);
                }
            });
    });

    }


    // Calling the functions to connect endpoints
    getInventory();
    getInventory_total_units();
    getRequests();
    getTransactions();
    url();
});
