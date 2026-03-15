# Bitacora 
En esta bitacora se estarán plasmando los resultados obtenidos a lo largo de todo el proceso, se tendra un registro de todos los hallazgos, dificultades y apredizajes. 

## Planteamiento del ejercicio: (definamos los parametros esenciales)
Eres el ingeniero aeronáutico encargado de programar el SMCS, un sistema básico a bordo de un bimotor comercial. El avión tiene una ruta programada que consta de un número de tramos (waypoints). Tu programa debe simular el vuelo, calculando el combustible restante después de cada tramo y tomando decisiones críticas si las reservas se ven comprometidas.

**Reglas del Sistema:**

1. **Capacidad Inicial:** El avión despega con un valor de combustible en el tanque en kilogramos.
2. **Consumo Base:** investiga cuál podría ser un consumo estándar en kilogramos por kilómetro.
3. **Efecto del Viento:**
    - Si hay viento en contra (Headwind), el consumo aumenta en “digamos” un 20%. Este valor, lo debes investigar tú y lo debes justificar. No puede ser el mismo de los otros grupos.
    - Si hay viento a favor (Tailwind), el consumo se reduce en `otro valor` que investigarás también.
    - Si el viento es cruzado o nulo, el consumo es el base.
4. **Reserva Legal:** El avión **nunca** puede bajar de un valor de combustible (este será el límite que tú debes definir). Si al proyectar el siguiente tramo el combustible caerá por debajo de este límite, el sistema debe emitir una alerta crítica, abortar la ruta y aterrizar en el aeropuerto alterno más cercano.

#### Solucion: 

**Tipo de avion** 

Para el desarrollo de este proyecto se eligió el **Airbus A320neo**, ya que es uno de los aviones de pasillo único más utilizados actualmente en la aviación comercial y también tiene una fuerte presencia en las operaciones aéreas dentro de Colombia. Muchas aerolíneas que operan en el país utilizan aeronaves de la familia A320 para cubrir rutas nacionales y regionales, por lo que resulta un modelo representativo para analizar aspectos relacionados con el consumo de combustible y la planificación de vuelo.

Además, el A320neo incorpora mejoras tecnológicas importantes orientadas a la eficiencia, como motores de nueva generación y optimizaciones aerodinámicas que reducen el consumo de combustible. Estas características lo convierten en una aeronave adecuada para estudiar cómo diferentes factores operacionales, como la distancia o el viento, pueden influir en el uso del combustible durante un vuelo.

**Hablemos un poco sobre el sistema de combustible** 

El A318, A319 y **A320** tienen el mismo diseño del sistema de combustible.
Los tanques de combustible están en la zona central del fuselaje y las alas. El tanque central es una parte de la caja central del ala. Los tanques de ala se dividen en células internas y las células exteriores, Para tener menos carga estructural en las alas.

en cuanto a células se refiere a compartimientos internos dentro de los tanques de conbustible del ala, diseñado para dividir el volumen total en secciones mas pequeñas y manejables para optimizar parametros como el centro de gravedad o incluso las operaciones de emergencia. 

**Un pequeño esquema sobre el sistema de combustible** 
![](../Imagenes/Imagen_15.png)

**¿Cuánto combustible suele llevar en operaciones reales?**

En operación normal los tanques casi nunca se llenan completamente.
Las aerolíneas cargan combustible según el plan de vuelo, que incluye:

- Combustible de ruta (trip fuel)

- Combustible de contingencia

- Combustible para aeropuerto alterno

- Reserva final

En rutas típicas de corto o medio alcance (1–3 horas), un A320neo suele despegar con aproximadamente:

        
        8 000 kg – 14 000 kg de combustible
        Para el programa se usara una medida de 10.000 kg
        Y el maximo de combustible sera de 18729 kg

En cuanto a el consumo en relacion kg-kilometro, asumiendo una velocidad crucero aprox:

        3 kg/km

Finalmente el combustible de emergencia que bajo ninguna circunstancia se debe consumir sera: 
        1200 kg
**Conclusiones en cuanto al combustible** 

Asumiremos estos valores como parametros iniciales para el programa: 

- Capacidad máxima ≈ 19 000 kg

- Carga típica operacional ≈ 8 000 – 14 000 kg

**Performance de vuelo** 
1. Viento en contra o cruzado (**neutral**): No hay modificaciones de consumo y el avion mantiene una velocidad crucero sin alteraciones. 

Porcentaje de ajuste = 0% 

2. Viento en contra (**headwind**): El viento en contra reduce la velocidad, lo que hace que el avión tarde más en recorrer la misma distancia. Como consecuencia, los motores trabajan durante más tiempo y el consumo total aumenta.

Porcentaje de ajuste = 18% (**Tailwind**): Cuando el viento sopla en la misma dirección del avión, la velocidad aumenta, el tiempo de vuelo se reduce y el consumo total disminuye.

Porcentaje de ajuste = -12%

|Condicion|Ajuste de consumo|Factor|
|---|---|---|
|Neutro|0%|1.00|
|Headwind|+18%|1.18|
|Tailwind|-12%|0.88|

## Fase 1: Análisis del problema y tabla de datos. 

#### Tabla de datos de entrada. 
|Datos|Descripción|
|---|---|
|combustible_inicial|Cantiddad de combustible con la que despegara el avion en kg|
|numero_tramos|Cantidad de tramos que tendra la ruta de vuelo|
|distancia_tramos|Distancia de cada tramo que el avion debe recorrer en km|
|tipo_viento|Condición del viento durante el tramo|
|destino_final|Lugar de detino donde aterrizara el avion|


### Tabla de datos de salida
|Datos|Descripción|
|---|---|
|consumo|Combustible consumido durante ese tramo|
|combustible_restante|Combustible que queda despues del tramo kg|
|alerta_reserva|Mensaje de alerta si el combustible llega al limite de seguridad|
|estado_vuelo|Indica si el vuelo continúa o si debe abortar|
|destino_final|Lugar de destino donde aterrizara el avion|

### Tabla de constantes
|Datos|Descripccion|
|---|---|
|consumo_base|Consumo estandar del avion (A320neo) en kg/km|
|factor_headwind|Incremento del consumo por viento en contra|
|factor_tailwind|Reducción de consumo por viento a favor|
|reserva_legal|Cantidad miníma de combustible que no debe gastarse en kg|

### Tabla de variables
|Datos|
|---|
|tipo_viento|
|consumo|
|estado_vuelo|
|numero_tramos|
|combustible_restante|
|destino_final|



## Pseudocodigo

        
                función calcular_consumo_tramo(distancia, viento)

                si viento es "headwind"
                        factor = factor_headwind
                sino si viento es "tailwind"
                        factor = factor_tailwind
                sino
                        factor = factor_neutro
        
        Inicio

                consumo_base = 3 kg/km
                factor_headwind = 1.18
                factor_tailwind = 0.88
                factor_neutro = 1
                reserva_legal = 1200 kg


        ingresar combustible_inicial
        ingresar numero_tramos
        ingresa  destino_final 
        combustible_actual = combustible_inicial


        para tramo desde 1 hasta numero_tramos

                mostrar: "Tramo {tramo}"
                ingresar distancia_tramos
                ingresar tipo_viento

                consumo = calcular_consumo_tramo(distancia_tramos, tipo_viento)
                combustible_actual = combustible_actual - consumo

                mostrar: "El consumo es: {consumo}"
                mostrar: "El combustible restante es: {combustible_actual}"

                si combustible_actual <= reserva_legal
                        Mostrar: "ALERTA combustible en reserva"
                        Mostrar: "Andate al aeropuesto más cercano"
                        break
                sino 
                        mostrar: "Vuelos completado con exito"
                fin si
        fin ciclo for

        si combustigle_actual >= reserva_legal
                mostrar "Has llegado a {destino_final} sin utilizar el combustible de reserva, buen trabajo"
        fin si

        fin

## Resultados finales

Se llevaron a cabo dos simulaciones, una en la cual el avion llegaria al aeropuerto con combustible suficiente y en otra donde debido a falta de combustible tendra que dirigirse al aeropuerto más cercano.

### Caso 1 
Destino: España

|Combustible|Tramo|Distancia|viento|Consumo|Combustible restante|
|---|---|---|---|---|---|
|30000|1|1200|headwind|4248|25752|
|25752|2|2000|neutro|6000|19752|
|19752|3|1800|tailwind|4752|15000|
|15000|4|1800|neutro|5400|9600|
|9600|5|1200|tailwind|3600|6000|

*Completado con exito*

**Resultado:**

![](../Imagenes/Imagen_16.png)

### Caso 2
Destino: Casablanca(Marruecos)

|Combustible|Tramo|Distancia|Viento|Consumo|Combustible restante|
|---|---|---|---|---|---|
|20000|1|1400|headwind|4956|15044|
|15044|2|1600|headwind|5664|9380|
|9380|3|1500|headwind|5310|4070|
|4070|4|2000|headwind|7080|**-3010**|
|---|---|---|---|---|---|

*A lo largo del tramo 4 es necesario abortar el vuelo por falta de combustible*

*Resultado:*
![](../Imagenes/Imagen_17.png)



