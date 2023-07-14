# plataforma_movil_ROS
Plataforma móvil desarrollada con ROS en una Raspberry Pi conectada a un Arduino, desde la cual se manejan los motores DC de la plataforma mediante una conexion SHH desde consola, además de evitar choques con obstáculos mediante el uso de sensores de ultrasonidos.

### Video:
  [![Plataforma móvil con ROS](https://img.youtube.com/vi/kSI_GsN-FN0/0.jpg)](https://youtu.be/kSI_GsN-FN0)
  
### Configurar WiFi raspberry:
1. Conectamos la raspberry al WiFi mediante un cable rj45 para que autoaticamente se le asigne una ip a la raspberyy
2. Obtenemos la ip asiganada de la raspberry y nos conectamos a ella mediante SHH
3. Accedemos al siguiene archivo
   ```shell
   sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
4. Modificamos el archivo con la ssid y contraseña del WiFi
   ```shell
   network={
    ssid="nombre_de_la_red"
    psk="contraseña_de_la_red"
   }
   
### Ejecutar nodos:
1. entramos en el working space del robot
   ```shell
   cd danipiWs/
3. Elegimos el espacio de trabajo
   ```shell
   source devel/setup.bash
4. Lanazamos el nodo de comunicación
   ```shell
   roscore
5. Ejecutamos el nodo del sensor de distancia
   ```shell
   rosrun sensor_distancia distancia.py
6. Ejecutamos el nodo para el control de los motores
   ```shell
   rosrun motor_control motores.py

### Dependencias:
   Para la comunicación entre la  Raspberry Pi y el Arduino hemos utilizado la biblioteca Pyserial para enviar y recibir datos entre ambos dispositivos a través de una conexión serial, lo cual posibilita el control y la transferencia de información en tiempo real.

- Pyserial: [Enlace al repositorio](https://github.com/nombre-de-usuario/pyseriañ)

