import { setupAjax, initializeRouteHandling } from './utils.js';
$(document).ready(function() {

    setupAjax();
    const authority = initializeRouteHandling();

    function url() {
        $("#dashboard_page").click(function(event){
            event.preventDefault();
                window.location.href =`http://127.0.0.1:8000/${authority}/dashboard`   // Redirect to the new URL
    });
        $("#inventory_page").click(function(event){
            event.preventDefault();
                window.location.href =`http://127.0.0.1:8000/${authority}/inventory`   // Redirect to the new URL
    });
        $("#requests_page").click(function(event){
            event.preventDefault();
                window.location.href =`http://127.0.0.1:8000/${authority}/requests`   // Redirect to the new URL
    });
        $("#request_form_page").click(function(event){
            event.preventDefault();
                window.location.href =`http://127.0.0.1:8000/${authority}/request_form`   // Redirect to the new URL
    });
    //     $("#logout").click(function(event){
    //         event.preventDefault();
    //             window.location.href =`http://127.0.0.1:8000/login`   // Redirect to the new URL
    // });
    }

    function logout(){
        $("#logout").click(function(event){
             event.preventDefault();

                $.ajax({
                    url: '/logout',
                    type: 'GET', // or 'POST' if your logout endpoint uses POST

                    success: function(response) {
                        localStorage.removeItem('accessToken');
                        // const route = window.location.pathname.replace('/', '');
                        // console.log(route)
                        localStorage.setItem('logoutMessage', 'Logged out successfully.');
                        window.location.href = '/login'
                    },
                    error: function(xhr) {
                        const errorData = xhr.responseJSON;
                        alert(`Logout failed: ${errorData.detail}`);
                    }
                });
            });        
    }

    url();
    logout();
});
