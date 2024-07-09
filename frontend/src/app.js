$(document).ready(function() {
    // Define your routes and associated stylesheets here
    const routes = {
      'hospital-dashboard': { page: 'hospitalDashboardPage', style: 'hospitalDashboard.css' },
      'blood-bank-dashboard': { page: 'bloodBankDashboardPage', style: 'bloodBankDashboard.css' },
      'login': { page: 'loginPage', style: 'login.css' },
      'signup': { page: 'signupPage', style: 'signup.css' },
      '': { page: 'loginPage', style: 'login.css' } // Default to login page
    };
  
    // Function to navigate to a page and load the corresponding stylesheet
    function navigateToPage(route) {
      const { page, style } = routes[route] || routes[''];
      $('#root').load(`/src/pages/html/${page}.html`, function() {
        $.getScript(`/src/pages/js/${page}.js`);
        $('#page-style').attr('href', `/src/assets/css/${style}`);
      });
    }

    $('#login-form').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way
        var username = $('#email').val();
        var password = $('#password').val();
        
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {email: email, password: password},
            success: function(response) {
                $('#root').html('<p>' + response.message + '</p>');
            },
            error: function(response) {
                $('#root').html('<p>' + response.responseJSON.detail + '</p>');
            }
        });
    });
  
    // // Simple routing logic
    // const path = window.location.pathname.replace('/', '');
    // navigateToPage(path);
  });
  