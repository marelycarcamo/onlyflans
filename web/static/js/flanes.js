document.addEventListener("DOMContentLoaded", function () {
    const descriptions = document.querySelectorAll(".card-text");
    descriptions.forEach((description) => {
        const readMoreBtn = description.nextElementSibling;
        const readLessBtn = readMoreBtn.nextElementSibling;

        // Verifica si el contenido del párrafo es más alto que su contenedor
        if (description.scrollHeight > description.clientHeight) {
            // Muestra el botón "Leer más" si el contenido es más largo
            readMoreBtn.style.display = "block";
            readMoreBtn.addEventListener("click", function () {
                // Muestra todo el contenido del párrafo
                description.style.webkitLineClamp = "unset";
                readMoreBtn.style.display = "none";
                readLessBtn.style.display = "block";
            });

            readLessBtn.addEventListener("click", function () {
                // Limita el contenido del párrafo a 4 líneas
                description.style.webkitLineClamp = "4";
                readMoreBtn.style.display = "block";
                readLessBtn.style.display = "none";
            });
        }
    });
});
