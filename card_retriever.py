def card_retrieve():
    import requests
    from bs4 import BeautifulSoup

    url_pagina = "https://cmll.com/cartelera/"

    headers_user = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Referer": "https://cmll.com/cartelera/",
    }

    # Solicitar la página web
    response = requests.get(url_pagina, headers=headers_user)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Buscar la etiqueta <img> con la clase específica 'event-card__image'
        imagen = soup.find("img", {"class": "event-card__image"})

        if imagen and "src" in imagen.attrs:
            url_imagen = imagen["src"]
            return url_imagen 
        else:
            # Si no se pudo descargar la imagen, muestra el código de estado y el mensaje del servidor
            print("No se pudo descargar la imagen")
    else:
                print("La etiqueta <img> no contiene un atributo 'src'.")