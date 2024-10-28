document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("menu-toggle");
    const dropdownMenu = document.getElementById("dropdownMenu");

    toggleButton.addEventListener("click", function() {
        // Alternar la visibilidad del menú
        dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
    });
});


// Inicializa el mapa
var map = L.map('map').setView([-34.6037, -58.3816], 13); // Coordenadas de CABA

// Capa de OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Control de búsqueda
var geocoder = L.Control.Geocoder.nominatim();

// Manejar el evento de entrada en la barra de búsqueda
document.getElementById('search').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        var query = this.value; // Obtener el valor del campo de búsqueda
        geocoder.geocode(query, function(results) {
            // Filtrar resultados para asegurarse de que estén dentro de CABA
            var foundInCABA = results.filter(function(result) {
                return result.properties && result.properties.address && result.properties.address.city === "Buenos Aires"; // Verificar que la ciudad sea CABA
            });

            if (foundInCABA.length > 0) {
                var latlng = foundInCABA[0].center; // Obtener las coordenadas del primer resultado
                map.setView(latlng, 13); // Centrar el mapa en la ubicación
                L.marker(latlng).addTo(map).bindPopup(foundInCABA[0].html || query).openPopup(); // Añadir marcador
            } else {
                alert("No se encontraron resultados en CABA para: " + query); // Mensaje si no se encuentran resultados
            }
        });
    }
});
