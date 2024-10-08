// Global AJAX setup to include Authorization header
export function setupAjax() {
    $.ajaxSetup({
        beforeSend: function(xhr) {
            var token = localStorage.getItem('accessToken');
            if (!token) {
                // xhr.setRequestHeader('Authorization', 'Bearer ' + token);
                window.location.href = '/login';
            }
            else{
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
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
        localStorage.setItem('Authorization_mssg', 'You were redirected bec. you are not authorized.');
        window.location.href = `/${place_name}/dashboard`;
        // alert("You are not authorized to do this action");
        
    } else if (route_list[0] !== "bloodbank" && role === "blood-bank-admin") {
        if (route_list[0] === "login" || route_list[0] === "register" || route_list[0] === "home" ){
            //pass
        }else{
            localStorage.setItem('Authorization_mssg', 'You were redirected bec. you are not authorized.');
            window.location.href = `/${place_name}/dashboard`;
            // alert("You are not authorized to do this action");
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
                localStorage.setItem('Authorization_mssg', 'You were redirected bec. you are not authorized.');
                window.location.href = `/${place_name}/dashboard`;
                // alert("You are not authorized to do this action");
            }
        }
    }

    return authority;
}

// Export the functions to be used in other files
