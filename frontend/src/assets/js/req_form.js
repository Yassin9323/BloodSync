import { setupAjax, initializeRouteHandling } from './utils.js';

$(document).ready(function() {
    setupAjax();
    const authority = initializeRouteHandling();

    $(document).on('submit', '#request-form', function(event) {
        event.preventDefault();
        
            $(document).on('click', '#submitBtn', function() {
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
                    },
                    error: function(xhr, status, error) {
                        console.error('Error updating status:', error);
                    }
                });
            });
    });
});