$(document).ready(function() {
    console.log("APP.JS")
    // Define your routes and associated stylesheets here
    const routes = {
      'dashboard': { page: 'dashboard', style: 'dashboard.css' },
      'error': { page: 'error', style: 'error.css' },
      'login': { page: 'login', style: 'login.css' },
      'register': { page: 'register', style: 'register.css' },
      '': { page: 'login', style: 'login.css' } // Default to login page
    };
    
    // Function to navigate to a page and load the corresponding stylesheet
    window.navigateToPage = function(route) {
      const { page, style } = routes[route] || routes[''];
      $('#root').load(`/static/public/${page}.html`, function() {
        $.getScript(`/static/src/assets/js/${page}.js`)
        .fail(function() {
          console.error(`Failed to load script: /static/src/assets/js/${page}.js`);
      });
        $('#page-style').attr('href', `/static/src/assets/css/${style}`);
      });
    }

    const route = window.location.pathname.replace('/', '');
    navigateToPage(route);
    console.log("Enter your acc ")


    function isValidEmail_1(email) {
      return email.includes('@');
    }
    function isValidEmail_2(email) {
      return email.includes('.com');
    }


    $(document).on('submit', '#login-form', function(event) {
            event.preventDefault(); // Prevent the form from submitting the traditional way

            var email = $('#email').val();
            var password = $('#password').val();

          let x = isValidEmail_1(email)
          let y = isValidEmail_2(email)
            // console.log("Login form submitted with:", { email, password });

            if(email && password && x && y ){
              $.ajax({
                url: '/login',
                type: 'POST',
                contentType: 'application/x-www-form-urlencoded',
                data: $.param({ email: email, password: password }),
        
                success: function(response) {
                    // console.log("Login successful, redirecting to dashboard...");           
                    window.location.href = '/blood-bank/dashboard';
                    },
                error: function(response) {
                    // console.log("Login failed (ajax error), redirecting to error page...");
                    // $("#login-result").alert("invaild credintials")
                    window.location.href = '/error';
        
                }
            });

            }
          
  });


  $(document).on('submit', '#register-form', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way
    var username = $('#username').val();
    var email = $('#email').val();
    var role = $('#role').val();
    var password = $('#password').val();
  
    let x = isValidEmail_1(email)
    let y = isValidEmail_2(email)
    // console.log("Login form submitted with:", { email, password });

    if(email && password && x && y ){
      $.ajax({
        url: '/register',
        type: 'POST',
        contentType: 'application/x-www-form-urlencoded',
        data: $.param({ email: email, username: username, password: password,  role: role }),

        success: function(response) {
            console.log("Login successful, redirecting to dashboard...");           
            window.location.href = '/login';
            },
        error: function(response) {
            console.log("Login failed (ajax error), redirecting to error page...");
            $("#register-result").text(response.responseJSON.detail).show();

        }
    });

    }
})
})