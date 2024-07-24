import { setupAjax, initializeRouteHandling } from './utils.js';
$(document).ready(function() {

    setupAjax();
    const authority = initializeRouteHandling();

     // WebSockets Realtime 
     const websocket = new WebSocket('ws://127.0.0.1:8000/ws/requests');

     websocket.onmessage = function(event) {
         const message = event.data;
        //  console.log(`WebSocket message received: ${message}`);
 
         switch (message) {
             case "pending_reqs_update":
                getPending_requests();
                 break;
             case "total_reqs_update":
                getTotal_requests();
                 break;
             case "update_status_update":
                updateRequest_status();
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

    // Function to access the Bloodbank_inventory endpoint
    function getPending_requests() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/requests/pending`,
            type: `GET`,
            success: function(response) {
                // console.log(`${authority} pending requests :`, response);
                // Handle the response data

                const req_pending = $('#req_pending');
                req_pending.empty(); // Clear existing table rows
                const data = response.pending_requests

                for(let i = 0; i < data.length; i++){
                    const firstItem = data[i];
                    const row = `<div class="pending-req">
                                    <div class="req-details">
                                        <p class="hospital-name">
                                            From:<span id="p_hospital_name">${firstItem.hospital_name}</span></p>
                                        <span class="details">Details:<span id="p_units">${firstItem.units} </span> Blood Bags of <span
                                                id="p_blood_type">${firstItem.blood_type}</span> Blood Type</span>
                                    </div>
                                    <div class="actin-buttons">
                                        <button id="approveBtn" class="request-action" data-action="approve" data-id="${firstItem.req_num}">Approve</button>
                                        <button id="declineBtn" class="request-action" data-action="decline" data-id="${firstItem.req_num}">Decline</button>
                                        <button id="redirectBtn" class="request-action" data-action="redirect" data-id="${firstItem.req_num}">Redirect</button>
                                    </div>
                                </div>`
                    req_pending.append(row);
                }

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
                // console.log(`${authority} total requests :`, response);
                // Handle the response data

                const req_history = $('#req_history');
                req_history.empty(); // Clear existing table rows
                const data = response.total_requests
                // console.log(data)
                for(let i = 0; i < data.length; i++){
                    const firstItem = data[i];
                    const row = `<div class="req-history">
                        <div class="req-details">
                            <p class="hospital-name">
                                From:<span id="h_hospital_name"> ${firstItem.hospital_name} </span></p>
                                <span class="details">Details:<span id="h_units"> ${firstItem.units} </span> Blood Bags of <span
                                id="h_blood_type"> ${firstItem.blood_type} </span> Blood Type</span>
                        </div>
                        <div class="req-status">
                            <span id="h_status"> ${firstItem.status.toUpperCase()} </span>
                        </div>
                    </div> `
                    req_history.append(row);
                }
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} total requests:`, status, error);
                // Handle the error
            }
        });
    }


    function updateRequest_status() {

        $(document).on('click', '.request-action', function() {
            var request_id = $(this).data('id');
            var action = $(this).data('action');
            
            console.log('Request ID:', request_id);
            console.log('Action:', action);

            $.ajax({
                url: `http://127.0.0.1:8000/${authority}/requests/update_status`,
                type: `POST`,
                contentType: "application/json",
                data: JSON.stringify({
                    request_id: request_id,
                    action: action
                    }),

                success: function(response) {
                    // Handle the response data
                    console.log("Sucessful");
                    const data =response.details
                    console.log(data);

                },
                error: function(xhr, status, error) {
                    if(authority === "bloodbank"){
                        console.error(`Error accessing Updting Status:`);
                    }
                }
            });
    });
    }

    // Call the function to access the endpoint
    getPending_requests();
    getTotal_requests();
    updateRequest_status();

});
