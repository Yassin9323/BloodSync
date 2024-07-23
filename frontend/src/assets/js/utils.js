// Global AJAX setup to include Authorization header
export function setupAjax() {
    $.ajaxSetup({
        beforeSend: function(xhr) {
            var token = localStorage.getItem('accessToken');
            if (token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
            }
            else{
                window.location.href = '/login';
            }
        }
    });
}

export function initializeRouteHandling() {
    var role = localStorage.getItem('role');
    var place_name = localStorage.getItem('place_name');
    
    // console.log(role);
    console.log(place_name);
    
    
    const route = window.location.pathname.replace('/', '');
    const route_list = route.split("/");
    // console.log(route_list[0]);
    let authority = null;

    if (route_list[0] === "bloodbank" && role === "blood-bank-admin") {
        authority = route_list[0];

    } else if (route_list[0] === "bloodbank" && role === "hospital-admin") {
        window.location.href = '/login';
        alert("You are not authorized to do this action");
        
    } else if (route_list[0] !== "bloodbank" && role === "blood-bank-admin") {
        if (route_list[0] === "login" || route_list[0] === "register" || route_list[0] === "home" ){
            //pass
        }else{
            window.location.href = '/login';
            alert("You are not authorized to do this action");
        }
        

    } else if (route_list[0] !== "bloodbank" && role === "hospital-admin") {    
        if (route_list[0] === place_name) {
            authority = route_list[0];
        } else {
            if (route_list[0] === "login" || route_list[0] === "register" || route_list[0] === "home" ){
                //pass
            }else{
                // console.log(route_list[0]);
                // console.log("3")
                window.location.href = '/login';
                alert("You are not authorized to do this action");
            }
        }
    }

    return authority;
}

// Export the functions to be used in other files
