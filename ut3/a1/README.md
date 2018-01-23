# Instalación de Wordpress y Configuración basíca.

### Acceso a la maquina de produccion.

Vamos al terminal y accedemos a la maquina de produccion vía **ssh**

![img](img/img1.png)

### Creación de base de datos.

Wordpress necesita un usuario/contraseña para acceder a la base de datos. Usaremos **MySQL**.

![img](img/img2.png)

Creamos la base de datos, el usuario y sus privilegios:

![img](img/img0.png)

### Descarga de código de Wordpress.

Vamos al terminal y con el comando ``curl -O https://Wordpress.org/latest.zip`` descargamos el código fuente de Wordpress.

![img](img/img3.png)

Descomprimimos el código y lo copiamos en la ruta ``/usr/share``

![img](img/img4.png)

![img](img/img5.png)

Ahora vamos a dar permiso a www-data para que pueda usar estos ficheros.

![img](img/img6.png)

> Usamos servidor web Nginx por eso le tenemos que dar los permiso a www-data.

### Configurar fichero de Wordpress.

Vamos a especificar el nombre de la base de datos, el usuario y contraseña, para que Wordpress lo pueda usar.

![img](img/img7.png)

> Usamos el fichero que nos da Wordpress como plantilla.

Modificamos el líneas siguientes.

![img](img/img8.png)

### Acceso mediante Nginx

Para poder acceder a nuestro sitio Wordpress desde un navegador Web , necesitamos incluir directivas necesarias en nuestro servidor web **Nginx**

Vamos a utilizar como acceso a Wordpress desde la url ``wordpress.alu4987.me``. Para ello creamos un nuevo host virtual.

![img](img/img10.png)

Ahora enlazamos el host virtual para que este disponible:

![img](img/img11.png)

Recargamos nuestro servidor para que los cambios se hagan efectivos.

![img](img/img12.png)

### Configuración de Wordpress vía web.

Accedemos mediante un nevegador Web ,con la direccion de nuestro sitio web ``http://wordpress.alu4987.me``.

![img](img/img13.png)

Elegimos el idioma y le damos a **Continuar**.

![img](img/img14.png)

Rellenamos los campos y **Instalar Wordpress**

![img](img/img15.png)

Pulsamos **Acceder** y iniciamos sesion.

![img](img/img16.png)

Y tenemos acceso a la interfaz de Wordpress.

![img](img/img17.png)

### Ajustes de Permalinks

En el panel administrativo de Wordpress, vamos a ajustes => Enlaces permanentes.

![img](img/img19.png)

Y seleccionamos el ajuste de **Dia y Nombre**. y Guardamos cambios.

![img](img/img18.png)

Ahora vamos a nuestro servidor web y indicamos a Nginx que procese estas URL:

![img](img/img20.png)

> Esta linea que añadimos es para procesar los Permalinks.

Recargamos nuestro servidor para que los cambios se hagan efectivos.

![img](img/img21.png)

> De esta manera podemos acceder a nuestro panel administrativo mediante http://wordpress.alu4987.me/admin

### Límite de tamaño en la subida de archivos.

Por defecto, el límite de subida de archivos para aplicaciones PHP suele ser bastante bajo, en torno a los 2MB.

Para incrementarlo, debemos modificar las siguientes líneas.

![img](img/img23.png)

Reiniciamos el servicio phph-fm.

![img](img/img24.png)

Y añadimos el la línea ``client_max_body_size 64M;`` en el fichero ``nginx.conf``

![img](img/img25.png)

Recargamos el servidor.

![img](img/img26.png)

### Creamos el primer post.

Vamos al panel administrativo y seleccionamos **Añadir nueva** y creamos nuestro post.

![img](img/img27.png)

Pulsamos en Actualizar para que se hagan efectivos los cambios.

![img](img/img28.png)
