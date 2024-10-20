document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("menu-toggle");
    const dropdownMenu = document.getElementById("dropdownMenu");

    toggleButton.addEventListener("click", function() {
        if (dropdownMenu.style.display === "none" || dropdownMenu.style.display === "") {
            dropdownMenu.style.display = "block";
        } else {
            dropdownMenu.style.display = "none";
        }
    });
});


 // Inicializa el mapa
 var map = L.map('map').setView([-34.6037, -58.3816], 13); // Coordenadas de CABA

 // Capa de OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

 // Marcadores en el mapa
var locations = [
    { name: "Parque Tres de Febrero", coords: [-34.5835, -58.4103] },
    { name: "Teatro Colón", coords: [-34.5885, -58.4173] },
    { name: "Casa Rosada", coords: [-34.6091, -58.3724] }
];

locations.forEach(function(location) {
    L.marker(location.coords)
        .addTo(map)
        .bindPopup(location.name)
        .openPopup();
});

 // Control de búsqueda
var geocoder = L.Control.Geocoder.nominatim();
var searchControl = new L.Control.Geocoder({
    defaultMarkGeocode: false
}).addTo(map);

searchControl.on('markgeocode', function(e) {
    var bbox = e.geocode.bbox;
    var latLng = e.geocode.center;
    L.marker(latLng).addTo(map).bindPopup(e.geocode.name).openPopup();
    map.fitBounds([bbox.getSouthWest(), bbox.getNorthEast()]);
});

 // Añadir el control de búsqueda al mapa
L.Control.geocoder().addTo(map);