from django.shortcuts import render


def index(request):

    temas = [
        {
            "id": 1,
            "nombre": "Gatos",
            "descripcion": "Los gatos son animales domésticos conocidos por su independencia, curiosidad y personalidad.",
            "url": "inicio:gatos"
        },
        {
            "id": 2,
            "nombre": "Baloncesto",
            "descripcion": "El baloncesto es un deporte en equipo donde los jugadores buscan anotar puntos en la canasta rival.",
            "url": "inicio:baloncesto"
        }
    ]

    return render(request, "inicio/inicio.html", {"temas": temas})


def gatos(request):

    tema = {
        "nombre": "Gatos",
        "descripcion": "Los gatos son animales domésticos conocidos por su independencia, curiosidad y personalidad."
    }

    return render(request, "inicio/gatos.html", {"tema": tema})


def baloncesto(request):

    tema = {
        "nombre": "Baloncesto",
        "descripcion": "El baloncesto es un deporte en equipo donde los jugadores buscan anotar puntos en la canasta rival."
    }

    return render(request, "inicio/baloncesto.html", {"tema": tema})