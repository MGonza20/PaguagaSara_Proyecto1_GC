# Proyecto 1 - Software Renderer - Gráficas por computadora

En el presente proyecto se buscó demostrar los conocimientos adquiridos en lo que ha transcurrido del curso de Gráficas por Computadora mediante renderización de modelos, aplicación de shaders y tranformaciones de los modelos. 

El tema de la escena renderizada fue: Vida Submarina. Se buscó aplicar 6 distintos shaders en los elementos puestos en la escena.  De los cuales se hablará más a continuación.

![Escene](https://user-images.githubusercontent.com/64711979/188372728-df472c68-fc6a-4986-b0f2-5c4f35616197.png)






## Shader: Estática (Escala de grises)

El objetivo de crear el shader de estática en escala de grises fue simular el efecto de que la estrella estuviera cubierta de arena.

![Static-Shader](https://user-images.githubusercontent.com/64711979/188356681-cd9a3257-9737-4181-b9ab-62a11f46c3b6.png)


## Shader: HSV 

El objetivo de crear este shader fue convertir los colores RGB (Rojo, Verde y Azul) a colores HSV(Tono, Saturación y Brillo), siendo los colores HSV otra representación de los colores RGB.  


![HSV-Shader](https://user-images.githubusercontent.com/64711979/188357615-a9f9c040-6db6-4134-a696-745b92a2a0d2.png)


## Shader: YIQ

El objetivo de crear este shader fue convertir los colores RGB (Rojo, Verde y Azul) al espacio de colores YIQ (Donde Y representa la información de luminancia, I fase y Q cuadratura). 

Para lograr esta conversión se multiplicó determinada matriz por el vector de las componentes del color RGB.


![YIQ-Shader](https://user-images.githubusercontent.com/64711979/188359136-a15ada1d-8762-432f-9293-93e320b3f40c.png)

**Fun fact:** Este espacio de color fue utilizado por el sistema análogo de color NTSC (National Television System Committee). 

## Shader: Normal

El propósito de este shader fue simular las imperfecciones de una superficie sin necesidad de que se hayan modelado en el modelo 3d que se renderizó.
**

![Normal-Shader](https://user-images.githubusercontent.com/64711979/188364003-5ca97102-518e-47f0-ba65-29a0a5b8c57a.png)

** Shader basado en ejemplo dado en clase.
## Shader: Oompa Loompa

El objetivo de este shader fue poder aplicar un cambio de color azul hacia pigmentos de un tono neón amarillo.

![OompaLoompa-Shader](https://user-images.githubusercontent.com/64711979/188370221-db641dff-da0b-4988-b380-b8b79ab0bf97.png)


## Shader: Negative

El propósito de este shader fue invertir los colores RGB y dar un efecto de imagen negativa.

![Negative-Shader](https://user-images.githubusercontent.com/64711979/188372495-dcdd06e1-aa5c-44e3-af21-53c502b71990.png)

## Ejecución del programa

Para ejecutar el programa solamente es necesario ejecutar el comando a continuación, esperar unos minutos y ver la escena generada en el archivo Escene.bmp.

```bash
  python Engine3D.py
```
