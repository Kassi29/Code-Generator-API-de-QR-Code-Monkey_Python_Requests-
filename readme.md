## Generador de Códigos QR Personalizados

Este es un script en Python que utiliza la API de QR Code Monkey para generar códigos QR personalizados con una variedad de opciones de personalización. Puedes utilizar este script para generar códigos QR para diferentes tipos de datos, como URL, texto plano, correo electrónico, teléfono y SMS.

### Clonación del Repositorio

Puedes clonar este repositorio ejecutando el siguiente comando en tu terminal:

```
git clone <URL_DEL_REPOSITORIO>
```

Pon la ruta exacta para que obtenga las imagenes para los logos
```
 files = {'file': open(f'[TU RUTA]/Code Generatots(API de QR Code Monkey_Python_Requests)/logo/{nombres_archivos[adjusted_option]}', 'rb')}
 ```
### Instalación de Dependencias

Asegúrate de tener instaladas las siguientes bibliotecas de Python antes de ejecutar el script:

- requests
- colorama

Puedes instalar estas dependencias ejecutando el siguiente comando:

```
pip install requests colorama
``` 
### Especificaciones de Personalización

El script te permite personalizar varios aspectos de tus códigos QR, incluyendo:

- Tipo de dato: selecciona el tipo de información que deseas codificar en el código QR.
- Forma del código QR: elige entre una variedad de formas para el código QR.
- Tamaño del código QR: especifica el tamaño del código QR en píxeles.
- Color del código QR: elige entre una variedad de opciones de color para el código QR.
- Diseño del ojo: selecciona el diseño del ojo del código QR.
- Diseño de la pupila: elige el diseño de la pupila del ojo del código QR.
- Logo: decide si deseas agregar un logo al código QR y elige entre varios logos disponibles.

### Descarga de los Códigos QR

Después de generar el código QR personalizado, tendrás la opción de descargarlo en formato PNG, SVG, PDF o EPS. Es importante tener en cuenta que los colores degradados no están disponibles en formato PDF.

Además, si prefieres obtener solo el enlace del código QR generado en lugar de descargarlo, puedes configurar la opción de descarga en "false".

### Directorio de Logos y Descargas

Si decides agregar un logo al código QR, asegúrate de colocar los archivos de logo en la carpeta de logos. Los códigos QR generados se descargarán en el mismo directorio donde se ejecuta el script.

### Captura
![Captura1](/img/consola1.PNG)
![Captura2](/img/consola2.PNG)
![Captura3](/img/consola3.PNG)



Con este script, podrás generar fácilmente códigos QR personalizados.

Si tienes mas preguntas puedes consultar:
https://www.qrcode-monkey.com/qr-code-api-with-logo/