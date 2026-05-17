document.addEventListener('DOMContentLoaded', function() {
    var oxford = [51.7520, -1.2577];
    var map = L.map('map').setView(oxford, 12);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 16,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    L.circle(oxford, {
        color: '#3498db',
        fillColor: '#3498db',
        fillOpacity: 0.12,
        radius: 2200
    }).addTo(map);
});
