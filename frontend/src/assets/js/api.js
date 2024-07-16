// // api.js

// // Function to fetch data from an endpoint
// export async function fetchData(endpoint) {
//     const accessToken = localStorage.getItem('accessToken');
//     try {
//         const response = await fetch(`http://localhost:8000${endpoint}`, {
//             headers: {
//                 Authorization: `Bearer ${accessToken}`,
//             },
//         });

//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }

//         return await response.json();
//     } catch (error) {
//         console.error('Fetch Error:', error);
//         throw error;
//     }
// }
