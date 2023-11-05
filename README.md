
# Rick & Morty API project

Este proyecto recoje informacion de la api de Rick & Morty y la muestra de forma mas ordenada y estetica al usuario.

El proyect esta echo con Flask.

Podemos encontrar un archivo .py, que contiene todas las funciones que recojen informacion de la API, y las muestrean en diversos HTML. Los HTML se encuentran en la carpeta templates, y el css que da estilo a todo el proyecto se encuentra en la carpeta static, junto a un archivo js, que sirve para cargar mas informacion en la pagina principal de la aplicacion web.

Al inicializar la aplicacion web con el comando "flask --app functions run", entraremos a la home. Aqui no encontraremos informacion, esta la encontraremos clickando a uno de los tres iconos que se nos muestran en la barra que hay a la izquierda de la pantalla.

El primer icono nos lleva a una pagina donde encontraremos todos los personajes disponibles en la api. De entrada solo cargan 20, pero hay un boton que nos permite cargar 12 mas. Se puede entrar a ver mas informacion de la que se muestra de cada personaje.

Los otros iconos nos llevan cada uno a una lista, de episodios o de localizaciones. Los titulos que encontraremos en las listas nos llevan a paginas en las que se nos muestran los personajes que salen en el episodio en concreto en al que hemos accedio, o los personajes que viven en la localizacion en la que hemos accedido.