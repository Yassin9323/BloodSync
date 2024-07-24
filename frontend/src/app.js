const file = window.location.pathname.replace('/', '');
var file_list = file.split("/");
if (!file_list[1]){
  import(`./assets/js/${file_list[0]}.js`)
} else {
  import(`./assets/js/${file_list[1]}.js`)
}
$(document).ready(function() {
  $('#error-message').hide();

  const route = window.location.pathname.replace('/', '');
  var route_list = route.split("/");
  var authority = route_list[0];
  var url_dashboard = `${authority}/dashboard`
  var url_inventory = `${authority}/inventory`
  var url_requests = `${authority}/requests`
  console.log("APP.JS")
  // console.log(route)
  // console.log(url_dashboard) // cairo_hospital/dashboard

  const routes = {
      [`${url_dashboard}`]: { page: 'dashboard', style: 'dashboard.css' },   // Navigating to any Dashboard page dynamically
      [`${url_inventory}`]: { page: 'inventory', style: 'inventory.css' },  // Navigating to any inventory page dynamically
      [`${url_requests}`]:  { page: 'requests', style: 'requests.css' },   // Navigating to any requests page dynamically
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
    navigateToPage(route);
});
