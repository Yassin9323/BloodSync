// Global AJAX setup to include Authorization header
export function setupAjax() {
    $.ajaxSetup({
        beforeSend: function(xhr) {
            var token = localStorage.getItem('accessToken');
            if (token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
            }
        }
    });
}

export function initializeRouteHandling() {
    var role = localStorage.getItem('role');
    var place_name = localStorage.getItem('place_name');

    if (place_name) { // Ensure place_name is not null
        place_name = place_name.replace('-', '_').toLowerCase();
    }

    // console.log(role);
    // console.log(place_name);
    
    
    const route = window.location.pathname.replace('/', '');
    const route_list = route.split("/");
    console.log(route_list[0]);
    let authority = null;

    if (route_list[0] === "bloodbank" && role === "blood-bank-admin") {
        authority = route_list[0];

    } else if (route_list[0] === "bloodbank" && role === "hospital-admin") {
        alert("Not Authorized \n You have to sign in with BloodBank account");
        window.location.href = '/login';
        
    } else if (route_list[0] !== "bloodbank" && role === "blood-bank-admin") {
        if (route_list[0] === "login" || route_list[0] === "register" || route_list[0] === "home" ){
            //pass
        }else{
            alert(`Not Authorized \n You have to sign in with ${route_list[0]} account`);
            window.location.href = '/login';
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
                alert(`Not Authorized \n You have to sign in with ${route_list[0]} account`);
                window.location.href = '/login';
            }
        }
    }

    return authority;
}

// Export the functions to be used in other files
