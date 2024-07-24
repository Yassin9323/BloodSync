import { setupAjax, initializeRouteHandling } from './utils.js';

$(document).ready(function() {
    setupAjax();
    const authority = initializeRouteHandling();

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
});