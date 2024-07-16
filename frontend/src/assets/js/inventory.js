$(document).ready(function() {
    async function fetchInventory() {
        const token = localStorage.getItem('accessToken');
        console.log("Retrieved token:", token); // Debugging line
        if (!token) {
            alert("You need to log in first.");
            window.location.href = '/'; // Redirect to login instead of register
            return;
        }

        try {
            const response = await fetch('/bloodbank/inventory/bank', { // Make sure the endpoint is correct
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (!response.ok) {
                throw new Error('Failed to fetch inventory');
            }

            const data = await response.json();
            displayInventory(data);
        } catch (error) {
            console.error("Fetch inventory error:", error); // Debugging line
            alert("Failed to fetch inventory. You may need to log in again.");
            window.location.href = '/'; // Redirect to login instead of register
        }
    }

    function displayInventory(data) {
        const inventoryElement = document.getElementById('inventory');
        inventoryElement.innerHTML = '';

        data.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.textContent = `Blood Type: ${item.blood_type}, Units: ${item.units}`;
            inventoryElement.appendChild(itemElement);
        });
    }

    fetchInventory();
});
