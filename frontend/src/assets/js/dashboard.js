import { setupAjax, initializeRouteHandling } from './utils.js';

$(document).ready(function() {
    setupAjax();
    const authority = initializeRouteHandling();

    // WebSockets Realtime 
    const websocket = new WebSocket('ws://127.0.0.1:8000/ws/dashboard');

    websocket.onmessage = function(event) {
        const message = event.data;
        console.log(`WebSocket message received: ${message}`);

        switch (message) {
            case "inventory_update":
                getInventory();
                break;
            case "inventory_total_units_update":
                getInventory_total_units();
                break;
            case "requests_update":
                getRequests();
                break;
            case "transactions_update":
                getTransactions();
                break;
            default:
                console.warn(`Unknown WebSocket message: ${message}`);
        }
    };

    websocket.onclose = function() {
        console.log('WebSocket connection closed');
        // Optional: Implement reconnection logic here
    };

    websocket.onerror = function(error) {
        console.log('WebSocket error: ' + error);
        // Optional: Implement error handling or reconnection logic here
    };

    // Function to access the blood bank inventory endpoint
    function getInventory() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/dashboard/inventory`,
            type: 'GET',
            success: function(response) {
                console.log(`${authority} inventory data:`, response);

                const tbody = $('.inventory-card table tbody');
                tbody.empty(); // Clear existing table rows
                const data = response.inventory;

                data.forEach(item => {
                    const row = `<tr>
                        <td>${item.blood_type}</td>
                        <td>${item.available_units}</td>
                    </tr>`;
                    tbody.append(row);
                });
                console.log(data);
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} inventory:`, status, error);
                // Optional: Implement retry or user notification here
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
                // Optional: Implement retry or user notification here
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
                // Optional: Implement retry or user notification here
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
                    console.log(item.hospital_name);
                });
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} transactions:`, status, error);
                // Optional: Implement retry or user notification here
            }
        });
    }

    // Initial data fetch
    getInventory();
    getInventory_total_units();
    getRequests();
    getTransactions();

    const route = window.location.pathname.replace('/', '');
    const route_list = route.split("/");
    var place_name = localStorage.getItem('place_name');

    const Authorization_mssg = localStorage.getItem('Authorization_mssg');
    if (Authorization_mssg && route_list[0] === place_name) {
        alert(Authorization_mssg);
        localStorage.removeItem('Authorization_mssg'); // Clear the message
    }
});
