document.addEventListener("DOMContentLoaded", function () {

    // Animación de entrada para las tarjetas
    const tarjetas = document.querySelectorAll(".tema-card");

    tarjetas.forEach((tarjeta, index) => {

        tarjeta.style.opacity = "0";
        tarjeta.style.transform = "translateY(30px)";

        setTimeout(() => {

            tarjeta.style.transition = "opacity 0.6s ease, transform 0.6s ease";
            tarjeta.style.opacity = "1";
            tarjeta.style.transform = "translateY(0)";

        }, 150 * index);

    });


    // Efecto al pasar el mouse por las imágenes
    const imagenes = document.querySelectorAll(".carousel img");

    imagenes.forEach((imagen) => {

        imagen.addEventListener("mouseenter", function () {
            imagen.style.transition = "transform 0.5s ease";
            imagen.style.transform = "scale(1.03)";
        });

        imagen.addEventListener("mouseleave", function () {
            imagen.style.transform = "scale(1)";
        });

    });

});