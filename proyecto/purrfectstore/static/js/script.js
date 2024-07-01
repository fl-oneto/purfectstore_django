document.addEventListener('DOMContentLoaded', function () {
    fetch("/api/cat-images/")
        .then(response => response.json())
        .then(data => {
            populateCategories(data);
        })
        .catch(error => console.error('Error fetching data:', error));

    // función agregar las imagenes al carrusel
    function populateCategories(data) {
        var container1 = document.getElementById("carrusel-gato1");
        var container2 = document.getElementById("carrusel-gato2");
        var container3 = document.getElementById("carrusel-gato3");

        // vaciar los contenedores antes de agregar nuevas img
        container1.innerHTML = '';
        container2.innerHTML = '';
        container3.innerHTML = '';

        // itera sobre cada imagen y la agrega al contenedor correspondiente
        data.forEach((image, index) => {
            var imageUrl = image.url;
            var imggato = document.createElement("img");
            imggato.src = imageUrl;
            imggato.classList.add('d-block', 'w-100'); 

            // agrega la imagen al contenedor correspondiente según el índice
            if (index === 0) {
                container1.appendChild(imggato);
            } else if (index === 1) {
                container2.appendChild(imggato);
            } else if (index === 2) {
                container3.appendChild(imggato);
            }
        });
    }
});