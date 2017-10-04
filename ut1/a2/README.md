# UT1-A2: Listado de directorios

## Preparación

Se creara una carpeta cuyo contenido son enlaces simbolicos que apuntan archivos del sistema,
se configura el archivo "sites-available" para poner un nueva localización.

###Creación de la carpeta y enlaces

Abrimos al terminal, entramos en nuestro dominio, vamos al "/home/aluxxxx" creamos la carpeta "Shared"

![image](img/ld1.png)

Ahora creamos dentro de la carpeta los enlaces simbolicos.

 ![image](img/ld3.png)

 Comprobamos que los enlaces se crearon bien

 ![imagen](img/ld4.png)

### Crear la localización

Vamos al archivo /sites-available y añadimos la nueva localización

![image](img/ld2.png)

Añadimos el autoindex para que nos cree un indice al acceder desde el navegador.

> Cuando se cambia algo en estos archivos siempre tenemos que hacer un reload del nginx

![image](img/ld5.png)

### Comprobación 

Abrimos el navegador y comprobamos que si cargo la configuracion del servidor

![image](img/ld6.png)
