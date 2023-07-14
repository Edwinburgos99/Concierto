# Programa ¿dónde pongo mi concierto?

El cantante Benito-G va a cantar en el Valle del Cauca y su concierto es muy apetecido. Cada ciudad quiere que el concierto quede lo más cerca posible de ellos. La gobernación ha decidido medir la distancia entre dos ciudades como la distancia Manhattan, que es la distancia en el eje X más en el eje Y. Nuestro departamento (Valle del Cauca), para efectos de simplificación, se representa como un cuadrado perfecto de N km por N km, siendo un plano donde X e Y son positivas; la esquina inferior izquierda marca la posición (0,0). En este sistema las ciudades están situadas sobre las intersecciones, es decir, siempre tienen posiciones enteras. Por ejemplo, si N = 10, una entrada posible sería:

|  Ciudad    |  X   |  Y   |
| :--------: | :--: | :--: |
| La Unión   |  1   |  9   |
|   Cali     |  3   |  9   |
|   Tuluá    |  2   |  7   |
| San Pedro  |  1   |  4   |

Sin embargo, con el fin de no alentar los duelos a muerte con cuchillos entre alcaldes, el concierto no puede quedar directamente dentro de una ciudad. Así mismo, tampoco puede quedar “favoreciendo” a una ciudad más que a otra, es decir, que el concierto debe quedar a una distancia donde sea relativamente equitativo, desplazarse, relativamente hablando.

Para la ejecución respectiva del programa en tu PC necesitarás tener instalado el programa Python (recomendación la versión más actual de Python), [Enlace_Descarga_Python](https://www.python.org/downloads/) en ese enlace podrá descargar el Python más actual. Una vez lo hayas instalado podrás proseguir con la instalación de las librerías necesarias para la ejecución del programa, librerías:

- pip install matplotlib
- pip install tk (normalmente viene instalado con el Python, pero en caso de que no, se puede instalar con el anterior comando)
- pip install Pillow

```
background_image = Image.open("C:\\Users\\Edwin\\Desktop\\Concert.png")
```

En la línea de código comentada se encuentra una dirección URL perteneciente a una imagen, corresponde a la imagen de fondo que use yo para el programa, como ustedes no cuentan con ella pueden dejar el fondo en blanco, o si quieren pueden descargar una imagen de internet, guardar la imagen en su PC (recomendación en escritorio) y el nombre colocado por ustedes en la imagen descargada cambiarlo en "Concert.png"

```
ruta_minizinc = "C:\\Users\\Edwin\\AppData\\Local\\Programs\\MiniZinc\\MiniZincIDE.exe"
```

En la línea de código comentada se encuentra una dirección URL correspondiente en donde yo guarde el archivo ejecutable del programa "minizinc". MiniZinc viene con un entorno de desarrollo integrado simple, el IDE de MiniZinc, que facilita el desarrollo y la ejecución de modelos de restricciones, por ello es usado para esta ocasión, puedes descargarlo haciendo clic en el siguiente enlace [Enlace_Descarga_Minizinc](https://www.minizinc.org/software.html), una vez allí solo debes buscar el que te funcione considerando el sistema operativo que uses. Una vez descargues el minizinc debes ir a la ubicación del archivo y pasar la respectiva dirección URL del archivo ejecutable "MiniZincIDE.exe".
