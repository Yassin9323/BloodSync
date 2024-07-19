$(document).ready(function() {
  $('#error-message').hide();

  $(document).ready(function() {
    // Global AJAX setup to include Authorization header
    $.ajaxSetup({
        beforeSend: function(xhr) {
            var token = localStorage.getItem('accessToken');
            if (token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
                console.log(token)
            }
        }
    });
    
  const route = window.location.pathname.replace('/', '');
  var route_list = route.split("/");
  var authority = route_list[0];
  var url_dashboard = `${authority}/dashboard`
  console.log("APP.JS")
  console.log(route)
  console.log(url_dashboard)
    // Define your routes and associated stylesheets here
    const routes = {
      [`${url_dashboard}`]: { page: 'dashboard', style: 'dashboard.css' },
      // 'cairo_hospital/dashboard': { page: 'dashboard', style: 'dashboard.css' },
      // 'bloodbank/dashboard': { page: 'dashboard', style: 'dashboard.css' },
      'bloodbank/inventory': { page: 'inventory', style: 'inventory.css' },
      'bloodbank/requests':  { page: 'requests', style: 'requests.css' },
      'error': { page: 'error', style: 'error.css' },
      'login': { page: 'login', style: 'login.css' },
      'register': { page: 'register', style: 'register.css' },
      // '': { page: 'login', style: 'login.css' },
      // Default to login page
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
    // Hello
    navigateToPage(route);
    console.log(page)
    console.log(style)
});
});
