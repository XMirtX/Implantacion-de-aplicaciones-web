# Aplicaciones Php y Python

* ## PHP

  * Creamos la carpeta PHP en ``mkdir /home/alu4987/PHP``
  * Subimos al servidor una pagina en php con el comando "**SCP**"

  ![image](img/img05.png)

  * Utilizamos el comando unzip para descomprimir el archivo.

  ![image](img/img06.png)

  * Vamos a la ruta ``/etc/nginx/sites-available`` y cremos un virtual host llamado php.

  ![image](img/img1.png)

  * Creamos un enlace simbolico en ``/etc/nginx/sites-enable`` para habilitar el virtual host.

  ![image](img/img03.png)

  * Hacemos un reload del servicio ``systemctl reload nginx.service`` y comprobamos en un navegador si funciona la pagina.

  ![image](img/img04.png)

* ## Python

  * Creamos una carpeta llamada "**now**" en la ruta ``/home/alu4987``

  ![image](img/img001.png)

  * Ahora creamos un entorno virtual para nuestras aplicaciónes.

  ![image](img/img002.png)

  * Activamos el entorno virtual para trabajar con el.

  ![image](img/img003.png)

  * Dentro del entorno instalamos con "**PIP**" ,"**UWSGI**" y "**FLASK**"

  ![image](img/img004.png)

  ![image](img/img005.png)

  * Creamos la app llamada ""**main.py**""

  ![image](img/img008.png)

  * Ahora vamos a crear un nuevo virtual host llamado "**now**" ``en /etc/nginx/sites-available`` y creamos el enlace simbolico en ``/etc/nginx/sites-enable`` para habilitar.

  ![image](img/img009.png)

  ![image](img/img010.png)

  * Ahora entramos en el entorno virtual y ejecutamos el proceso para escuchar peticiones para nuestra app ``uwsgi --socket 0.0.0.0:8080 --protocol=http -w main:app``

  ![image](img/img011.png)

  * Comprobamos en el navegador <http://now.alu4987.me>

  ![image](img/img012.png)

* ## Configuración del servidor web uWSGI

  * Configuramos el servidor web uwsgi, creando un fichero "**uwsgi.ini**" que sera el encargado de ejecutar la app.

  ![image](img/img013.png)

  * Ahora creamos un pequeño script llamado "**run.sh**" que se encarga de activar nuestro entorno virtual de nuestra aplicación y ejecuar el uwsgi.ini.

  ![image](img/img014.png)

  * Le damos permiso de ejecución al script.

  ![image](img/img015.pnf)

  * Hacemos un reload del servidor para que carge la nueva información.

  * Ejecutamos el script y comprobamos en el nevegador que se esta ejecutando la aplicación.

  ![image](img/img016.png)

  ![image](img/img017.png)

* ## Supervisor

  * Usaremos una herramienta de cordinador de procesos "**Supervisor**" que se encarga de mantener activa nuestra aplicación.

  * Creamos una configuración para supervisor para que cordine nuestra app.

  ![image](img/img018.png)

  * Ahora hacemos un restart de supervisor para que carge la nueva configuración y comprobamos que esta activa.

  ![image](img/img019.png)

  * Comprobamos que esta activa nuestra aplicación accediendo por el navegador.

  ![image](img/img017.png)

  * Hacemos un ``supervidorctl stop now``.

  ![image](img/img020.png)

  * Comprobamos y si la aplicación no esta funcionando.

  ![image](img/img021.png)

  * Volvemos a activarlo ``supervidorctl start now``.

  ![image](img/img022.png)

  * Comprobamos que funciona.

  ![image](img/img017.png)

  * Hacemos ``supervidorctl restart now`` y volvemos a comprobar que funciona perfectamente.

  ![image](img/img024.png)

  ![image](img/img017.png)
