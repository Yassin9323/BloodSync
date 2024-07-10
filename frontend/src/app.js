$(document).ready(function() {
    console.log("Ajaxxxxxxxx")
    // Define your routes and associated stylesheets here
    const routes = {
      'hospital-dashboard': { page: 'hospitalDashboardPage', style: 'hospitalDashboard.css' },
      'blood-bank-dashboard': { page: 'bloodBankDashboardPage', style: 'bloodBankDashboard.css' },
      'login': { page: 'login', style: 'login.css' },
      'signup': { page: 'signupPage', style: 'signup.css' },
      '': { page: 'login', style: 'login.css' } // Default to login page
    };
  
    // Function to navigate to a page and load the corresponding stylesheet
    function navigateToPage(route) {
      const { page, style } = routes[route] || routes[''];
      $('#root').load(`/static/public/${page}.html`, function() {
        // $.getScript(`/frontend/src/pages/js/${page}.js`);
        $('#page-style').attr('href', `/static/src/assets/css/${style}`);
      });
    }

    $('#login-form').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way
        var email = $('#email').val();
        var password = $('#password').val();
        
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {email: email, password: password},
            success: function(response) {
              window.location.href = '/dashboard'
            },
            error: function(response) {
              window.location.href = '/error'
            }
        });
    });
  
    // // Simple routing logic
    // const path = window.location.pathname.replace('/', '');
    // console.log(path)
    // navigateToPage(path);
  });
  