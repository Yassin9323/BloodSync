$(document).ready(function() {
  $('#error-message').hide();
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
    // Hello
    const route = window.location.pathname.replace('/', '');
    navigateToPage(route);
});
