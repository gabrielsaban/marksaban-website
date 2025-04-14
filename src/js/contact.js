document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map
    var map = L.map('map').setView([51.7413254, -1.2567501], 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 16,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add a marker to the map
    var marker = L.marker([51.7413254, -1.2567501]).addTo(map);
}); 