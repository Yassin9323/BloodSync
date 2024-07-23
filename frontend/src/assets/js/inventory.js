import { setupAjax, initializeRouteHandling } from './utils.js';
$(document).ready(function() {

    setupAjax();
    const authority = initializeRouteHandling();
    
    // Function to access the Bloodbank_inventory endpoint
    function get_inventory() {
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/inventory/`,
            type: 'GET',
            success: function(response) {
                console.log(`${authority} inventory:`, response);
                // Handle the response data
                const inv_h = $('#inv-table-bank thead tr');
                const data = response.inventory.inventory_data
                data.forEach(item => {
                    const row = `
                        <th>${item.blood_type}</th>`; 
                        inv_h.append(row);
                });


                const inv_b = $('#inv-table-bank tbody tr');
                inv_b.empty(); // Clear existing table rows
                const data_name = response.inventory.name
                const name = `<td>${data_name}</td>`
                inv_b.append(name);
                data.forEach(item => {
                    const row = `
                        <td>${item.available_units}</td>`; 
                        inv_b.append(row);
                });


            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} inventory:`, status, error);
                // Handle the error
            }
        });
    }

    // Function to access the Hospital_inventory endpoint
    // $('#select_hospital').on('change', function() {
    function getHospital_inventory() {
        $('#select_hospital').on('change', function() {
            const hospitalName = $(this).val();
            console.log("Selected Hospital:", hospitalName);
        $.ajax({
            url: `http://127.0.0.1:8000/${authority}/inventory/${hospitalName}_inventory`,
            type: 'GET',
            success: function(response) {
                // const inv_h = $('#inv-table-hospital thead tr');
                // inv_h.empty(); // Clear existing table rows
                const data = response.details.inventory
                // data.forEach(item => {
                //     const row = `
                //         <th>${item.blood_type}</th>`; 
                //         inv_h.append(row);
                // });


                const inv_b = $('#inv-table-hospital tbody tr');
                inv_b.empty(); // Clear existing table rows
                const data_name = response.details.name
                const name = `<td>${data_name}</td>`
                inv_b.append(name);
                data.forEach(item => {
                    const row = `
                        <td>${item.available_units}</td>`; 
                        inv_b.append(row);
                });


            },
            error: function(xhr, status, error) {
                if (authority === "bloodbank"){
                    console.error("Error accessing hospital inventory:", status, error);
                }                
            }
        });
    // }  
});

    }

    // Call the function to access the endpoint
    get_inventory();
    getHospital_inventory();
});
