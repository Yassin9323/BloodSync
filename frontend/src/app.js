$(document).ready(function() {
    console.log("APP.JS")
    // Define your routes and associated stylesheets here
    const routes = {
      'dashboard': { page: 'dashboard', style: 'dashboard.css' },
      'error': { page: 'error', style: 'error.css' },
      'login': { page: 'login', style: 'login.css' },
      'signup': { page: 'signupPage', style: 'signup.css' },
      '': { page: 'login', style: 'login.css' } // Default to login page
    };
    
    // Function to navigate to a page and load the corresponding stylesheet
    window.navigateToPage = function(route) {
      const { page, style } = routes[route] || routes[''];
      $('#root').load(`/static/public/${page}.html`, function() {
        // $.getScript(`/static/src/pages/js/${page}.js`);
        $('#page-style').attr('href', `/static/src/assets/css/${style}`);
      });
    }

    const route = window.location.pathname.replace('/', '');
    navigateToPage(route);
    console.log("Enter your acc ")

    $(document).on('submit', '#login-form', function(event) {
      event.preventDefault(); // Prevent the form from submitting the traditional way

      var email = $('#email').val();
      var password = $('#password').val();

      console.log("Login form submitted with:", { email, password });

      $.ajax({
        url: '/login',
        type: 'POST',
        contentType: 'application/x-www-form-urlencoded',
        data: $.param({ email: email, password: password }),

        success: function(response) {
            // console.log("Login successful, redirecting to dashboard...");           
            window.location.href = '/dashboard';
            },
        error: function(response) {
            // console.log("Login failed (ajax error), redirecting to error page...");
            // $("#login-result").alert("invaild credintials")
            window.location.href = '/error';

        }
    });
  });
})
  