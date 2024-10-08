import { setupAjax, initializeRouteHandling } from './utils.js';

$(document).ready(function() {
    setupAjax();
    const authority = initializeRouteHandling();

     // WebSockets Realtime 
     const websocket = new WebSocket('ws://127.0.0.1:8000/ws/create_request');

     websocket.onmessage = function(event) {
         const message = event.data;
        //  console.log(`WebSocket message received: ${message}`);
 
         switch (message) {
             case "create_reqs_update":
                create_request();
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


    function create_request(){
    $(document).on('submit', '#request-form', function(event) {
        event.preventDefault();
        
            // $(document).click('#submitBtn', function() {
                const blood_type = $('#blood_type').val();
                const requested_units = $('#units').val();
                console.log('Selected Blood Type:', blood_type);
                console.log('Selected units:', units);

                $.ajax({
                    url: `http://127.0.0.1:8000/${authority}/requests/create_request`,
                    type: 'POST',
                    contentType: 'application/x-www-form-urlencoded',
                    data: $.param({ blood_type: blood_type, requested_units: requested_units}),

                    success: function(response) {
                        console.log('Successful');
                        const data = response;
                        console.log(data);

                        // Show the message div
                        $('.message').removeClass('hidden').addClass('show');
                
                        // Check if the class is applied
                        console.log('Message class after adding show:', $('.message').attr('class'));

                        // Hide the message div after 3 seconds
                        setTimeout(function() {
                            $('.message').removeClass('show').addClass('hidden');
                            
                            // Check if the class is applied
                            console.log('Message class after removing show:', $('.message').attr('class'));
                        }, 3000);
                    },
                    error: function(xhr, status, error) {
                        console.error('Error updating status:', error);
                    }
                });
            // });
    });
};
    create_request();
});