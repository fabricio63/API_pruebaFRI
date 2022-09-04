# API de prueba para Fri


## Requerimiento
  Debe crearse una API que centralice otros servicios de búsqueda para que quién consuma el servicio tenga
  un solo endpoint en donde coloque su criterio de búsqueda y esta API realice búsquedas en otros servicios,
  las consolide, las ordene y les coloque un solo formato de resultado indicando cuál es el origen en donde se
  encontró la coincidencia.
  
Debe crearse documentación de esta API para que cualquiera que quiera integrarse a ella pueda hacerlo sin
necesidad de capacitaciones o explicaciones personales.

## Fuentes
Las fuentes de búsqueda pueden incluir servicios REST y SOAP e inicialmente estos son los endpoints que
pueden incluirse en la solución:

- https://itunes.apple.com/search?term=jack+johnson
    - canciones
    - películas


  documentación del servicio
  https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html#//apple_ref/doc/uid/TP40017632-CH5-SW1


- http://www.tvmaze.com/api
  - shows de televisión
  - http://www.crcind.com/csp/samples/SOAP.Demo.cls
  - personas

## Entregables
- Código fuente
- Documentación de API
- Documento que explique cómo realizar la prueba asumiendo que se realizará la misma en un
  ambiente linux limpio, es decir, sin ningun paquete específico para desarrollar o correr aplicaciones,
  por lo tanto deben incluirse dependencias y versiones específicas si se requiere
 
## Evaluación
Se evaluarán los siguientes puntos
  - Nivel de abstracción
  - Separation of Concerns
  - Respuestas del servicio
  - Documentación


## Instrucciones para correr el API

### Requisitos para poder ejecutar la aplicacion

  - Se debe tener docker instalado en una maquina linux basado en una arquitectura intel (la aplicacion no puede ser ejecutada en una computadora con arquitectura ARM)
  - Se debe tener el docker daemon inicializado, posteriormente solo se debe seguir los siguientes comandos para ser ejecutada
  
### 1
Se ejecuta el comando para descargar la imagen desde DockerHub:

- sudo docker pull fabricio2000gjuarez/pythonapp:latest

### 2 
Se ejecuta el siguiente comando para levantar el contenedor en la maquina local:

- sudo docker run -d -it -p 80:80 fabricio2000gjuarez/pythonapp:latest 

### 3

Para comprobar el correcto funcionamiento de la aplicacion se debe ir a su browser e ingresar a localhost:80/home donde se podra ver la aplicacion demo con una interfaz grafica 


