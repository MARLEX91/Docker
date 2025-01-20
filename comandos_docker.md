# Comados Docker

## Comando imagenes

- **docker pull** "nombre_imagen":version --> descargan una imagen especifica de docker hub.

- **docker images** mustra información sobre las imagenes descagadas o contruidas.

- **docker rmi "nombre imagen"** eliminar imagen especificada

## Comandos contenedores

- **docker create "nombre imagen"** crear un contenedor con unaimagen especifica ej: docker create mongo.

- **docker start "container_id"** arrancar contenedor existente.

- **docker ps** mostrar listado de contenedores en ejecución.

- **docker ps -a** mostrar listado de todos los contenedores creados.

- **docker rm "container_id or name"** elimina el contendor indicado.

- **docker stop "container_id or nombre de contenedor"** detiene la ejecución del contenedor especificado

- **docker create --name "nombre contendor"** crear un contenedor y asignarle un nombre especifico.

- **docker create -p"puerto_host:puerto_contenedor" --name** crear un contenedor, mapear puertos del anfitrion:puertos del contendor y asignar nombre. ej: docker create -p27017:27017 --name mongoapp, si no se especifica el puerto de host docker, escojerá uno por nosostros, ej: docker create -p27017 --> aqui solo pasamos el puertoque queremos mapear del contenedor. 

- **docker logs "container_id or nombre contedor"** ver los log de ejecución de un contenedor en especifico. Si necesitamos que el docker se quede escuchando los logs de un contendor agregaremos la etiqueta de follow. ej docker logs --follow

- **docker run "nombre_imagen"** este comando nos ayuda a realiza la creación de una imagen y la ejecución en un contendor de manera rapida.
 - primero valida si la imagen indicada existe, si no, la descaga
 - segundo crea el contenedor.
 - tercero inicia el contenedor, lo ejecuta

 el problema con este comando es que cuando ejecuta el contenedor lo ejecuta en modo logs follow y se queda escuchando el contenedor y si presionado Ctrl+c para salirnos del modo follor se detiene la ejecución del contenedor, si queremos evitar esto al ejeutar docker run debemos agregar la etiqueta follow como se muestra en el siguiente comando.

- **docker run -d "imagen"** descarga la imagen y la ejecuta en un contenedor pero no entra en modo follow si no en modo detach, solo nos devuelve el id del contenedor que se creó y que esta en ejecución.

- **docker create -e "nombre_vble_entorno=valor"** este comando permite crear un contenedor, crer varibles de entorno y su respectivo valor ej MONGO_INITDB_ROOT_USERNAME=ALEX. Esta etiqueta se debe de escribir tantas veces como parametros se ingresen.

### Ejemplo de docker create con todas las etiquetas:
docker create  -p3000:3000 --name chanchito --network mired miapp:1
notese: 
-p = define puertos host y contenedor a mapear respectivamente 
-- name = signa nombre a contenedor.
--network = especifica la red a la que va a pertenecer el contendor
miapp = nombre de la imagen con la que se creará el contenedor
:1 = versión que se le quiera asignar

## docker compose

- **docker compose up** este comando ejecuta docker compose y levanta los contenedores que se especifican en el archivo docker-compose.yml. Este comando se debe de ejecutar en la misma ruta donde se haya creado el archivo docker-compose.yml

- **docker compose down** este comando detiene la ejecución de los contenedores que se levantaron con el comando anterior.