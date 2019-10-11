# Instalar Odoo 12 para desarrollo en Ubuntu 18.04 usando Pycharm

Espero esta guia ayude a quien lo necesite y un agradecimiento para Hanish Mangalasseri y su blog por la información brindad

**https://odooforbeginners.blogspot.com/2019/06/odoo-12-development-in-ubuntu-1804.html**


## Actualiza el sistema primero
>sudo apt-get update
>sudo apt-get -y upgrade

## Instalar las dependencias de Python para Odoo 12
>sudo apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less

## Instalando Pycharm

Para instalar Pycharm, se tiene 2 formas de realizarlo:
Instalar Pycharm en Ubuntu 18.04 por comandos
>sudo snap install pycharm-community --classic

O puede descargarlo de

[https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux) .

Después de descargar Pycharm, debe ir a la carpeta bin, abrir el terminal alli y escribir

>pycharm.sh file using ./pycharm.sh

Otra alternativa es descargar el Pycharm CE usando el centro de software de Ubuntu como se muestra en la imagen de aquí abajo

![enter image description here](https://1.bp.blogspot.com/-G7yxpf1E_gg/XPOpzzMhwRI/AAAAAAAABVs/kiGp10LMBGAHNQjzz41ny2vWSobKoplRgCLcBGAs/s1600/screenshot-linuxize.com-2019.06.02-16-19-17.png)
## Instalando Postgresql

>sudo apt update
>sudo apt install postgresql postgresql-contrib

## Creando un nuevo rol en Postgres
>sudo -u postgres createuser --interactive

## Salida
>Enter name of role to add: odoo
>Shall the new role be a superuser? (y/n) y

## Crear password para el nuevo rol
>sudo -u postgres psql
>ALTER ROLE odoo WITH PASSWORD 'odoo';
>para salir usar '\q'

## Descargar Odoo 12
Para poder descargar la última version de Odoo en zip de Github o clonar el código fuente de Odoo de github tiene que realizarlo desde el Pycharm

[https://github.com/odoo/odoo/archive/12.0.zip](https://github.com/odoo/odoo/archive/12.0.zip)

Despues de extraer el archivo zip, debemos ir a la carpeta raiz e instalar el archivo de requerimientos a través del terminal usando la sentencia

>pip3 install -r requirements.txt

Se deberá crear el archivo de configuración de Odoo dentro del directorio de Odoo
Copiar y pegar el contenido en el archivo de configuración, se deberá agregar los paths correctos de su directorio
>[options]
;:admin_passwd = admin
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
xmlrpc_port = 8069
>addons_path = /home/hanish/odoo/odoo-12.0/addons,/home/hanish/odoo/odoo-12.0/odoo/addons

En el menu de Pycharm **Run**>**Edit** Configurations, debemos agregar **+** en la pestaña superior a la izquierda para crear una nueva configuracion con las siguientes sentencia, tal y como presenta la imagen.

![enter image description here](https://1.bp.blogspot.com/-ETz1-8iyLu8/XPPCH11bAwI/AAAAAAAABWE/uVL7ZBT7enUWzUvDIbNtkXKzl7dssbnHACLcBGAs/s640/Screenshot+from+2019-06-02+17-41-32.jpg)
**Ir al navegador e ingresar al localhost:8069 para poder acceder a Odoo12, en la pantalla que se muestra aquí abajo podremos crear la base de datos con la cual trabajaremos**

![enter image description here](https://1.bp.blogspot.com/-2WYZADv_T9w/XPPEjVVQlwI/AAAAAAAABWQ/u5Gaqe6vw6o0WEilBjcFZ7QAPIYw2BRwACLcBGAs/s400/screenshot-0.0.0.0-8069-2019.06.02-17-44-24.png)




