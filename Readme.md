# Programa ¿donde pongo mi concierto?

El cantante Benito-G va a cantar en el Valle del Cauca y su concierto es muy apetecido. Cada ciudad quiere que el concierto quede lo mas cerca posible de ellos. La gobernacion ha decidido medir la distancia entre dos ciudades como la distancia Manhattan, que es la distancia en el eje X mas en el eje Y. Nuestro departamento (Valle del Cauca), para efectos de simplificacion, se representa como un cuadrado perfecto de N km por N km, siendo un plano donde X e Y son positivas; la esquina inferior izquierda marca la posicion (0,0). En este sistema las ciudades estan situadas sobre las intersecciones, es decir siempre tienen posiciones enteras. Por ejemplo, si N = 10 una entrada posible serıa:

|  Ciudad   |  X  |  Y  |
| :-------: | :-: | :-: |
| La Union  |  1  |  9  |
|   Cali    |  3  |  9  |
|   Tulua   |  2  |  7  |
| San Pedro |  1  |  4  |

Sin embargo, con el fin de no alentar los duelos a muerte con cuchillos entre alcaldes, el concierto no puede quedar directamente dentro de una ciudad. Ası mismo, tampoco puede quedar “favoreciendo” a una ciudad mas que a otra, es decir que el concierto debe quedar a una distancia donde sea relativamente equitativo desplazarse, relativamente hablando.

Para la ejecucion respectiva del programa en tu PC necesitaras tener instalado el programa python (recomendacion la version mas actual de python), [Enlace_Descarga_Python](https://www.python.org/downloads/) en ese enlace podra descargar el python mas actual. Una vez lo hayas instalado podras proseguir con la instalacion de las librerias necesarias para la ejecucion del programa, librerias:

- pip install matplotlib
- pip install tk (normalmente viene instalado con el python pero en caso de que no, se puede instalar con el anterior comando)
- pip install Pillow

```
background_image = Image.open("C:\\Users\\Edwin\\Desktop\\Concert.png")
```

En la linea de codigo comentada se encuentra una direccion url perteneciente a una imagen, corresponde a la imagen de fondo que use yo para el programa, como ustedes no cuentan con ella pueden dejar el fondo en blanco, o si quieren pueden descargar una imagen de internet guardar la imagen en su PC (recomendacion en escritorio) y el nombre colocado por ustedes en la imagen descargada cambiarlo en "Concert.png"

```
ruta_minizinc = "C:\\Users\\Edwin\\AppData\\Local\\Programs\\MiniZinc\\MiniZincIDE.exe"
```

En la linea de codigo comentada se encuentra una direccion url correspondiente en donde yo guarde el archivo ejecutable del programa "minizinc". MiniZinc viene con un entorno de desarrollo integrado simple, el IDE de MiniZinc, que facilita el desarrollo y la ejecución de modelos de restricciones, por ello es usado para esta ocasion, puedes descargarlo haciendo click en el siguiente enlace [Enlace_Descarga_Minizinc](https://www.minizinc.org/software.html), una vez alli solo debes buscar el que te funcione considerando el sistema operativo que uses. Una vez descargues el minizinc debes ir a la ubicacion del archivo y pasar la respectiva direccion url del archivo ejecutable "MiniZincIDE.exe".
