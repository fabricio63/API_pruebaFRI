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
    -canciones
    -películas


  documentación del servicio
  https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearch API/Searching.html#//apple_ref/doc/uid/TP40017632-CH5-SW1


- http://www.tvmaze.com/api
  - shows de televisión
  - http://www.crcind.com/csp/samples/SOAP.Demo.cls
  - personas

#Entregables
- Código fuente
- Documentación de API
- Documento que explique cómo realizar la prueba asumiendo que se realizará la misma en un
- ambiente linux limpio, es decir, sin ningun paquete específico para desarrollar o correr aplicaciones,
  por lo tanto deben incluirse dependencias y versiones específicas si se requiere
