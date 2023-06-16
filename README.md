# Mundial

Mundial es un lenguaje de consulta diseñado para obtener información sobre la Copa del Mundo de la FIFA. Permite realizar consultas relacionadas con jugadores, equipos y datos estadísticos de los diferentes mundiales.

## Uso

El lenguaje Mundial se utiliza a través de la línea de comandos con la siguiente sintaxis:

`mundial [opcion] [argumento]`

### Opciones

El lenguaje Mundial admite las siguientes opciones:

1) `mundial -h “jugador”` (lista los goles del jugador en mundiales)*
2) `mundial -t "pais"` (muestra la cantidad de veces que el pais ha ganado la Copa del Mundo)*
3) `mundial -g "año_mundial"` (muestra la cantidad total de goles anotados en ese mundial)*
4) `mundial -c "año_mundial"` (muestra el campeón del mundial de ese año)*
5) `mundial -m "pais"` (muestra el promedio de goles del pais en los mundiales en los que ha participado)*
6) `mundial -p "jugador"` (muestra el mundial donde mas goles ha metido el jugador)*
7) `mundial -j "año_mundial"` (muestra el goleador del mundial de ese año)*

### Ejemplos de Uso

Aquí hay algunos ejemplos de cómo usar el lenguaje Mundial:

`mundial -j "2010"` muestra el goleador del mundial del 2010.

`mundial -h "Ronaldo"` Lista los goles anotados por Cristiano Ronaldo en los mundiales.

`mundial -t "Alemania"` Muestra la cantidad de veces que Alemania ha ganado la Copa del Mundo.

### Restricciones y casos de error
Es importante tener en cuenta algunas restricciones y casos de error al utilizar el lenguaje Mundial. En primer lugar, asegúrate de escribir correctamente el comando y las opciones, ya que cualquier error tipográfico puede generar un resultado inesperado o producir un error. Además, ten en cuenta que el lenguaje Mundial es sensible a mayúsculas y minúsculas, por lo que debes escribir los comandos y las consultas de forma precisa.

Además, ten en cuenta que si proporcionas un año incorrecto, es posible que no se muestren los resultados esperados o se produzca un error. Asegúrate de ingresar correctamente los años de los mundiales para obtener la información correcta. En caso de que se produzca un error, el lenguaje Mundial mostrará un mensaje de error descriptivo indicando la naturaleza del problema. Presta atención a estos mensajes de error para identificar y corregir los errores en tu consulta.

Recuerda revisar la documentación y los ejemplos proporcionados para comprender mejor el formato y las opciones admitidas por el lenguaje Mundial. Esto te ayudará a evitar errores y obtener los resultados deseados de manera más efectiva.