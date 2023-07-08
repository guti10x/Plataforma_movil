#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import serial
import time

def read_ultrasound_data():
    rospy.init_node('direction_publisher', anonymous=True)

    port = '/dev/ttyACM0'  # Puerto serial al que está conectado el Arduino
    baud_rate = 9600  # Velocidad de comunicación

    while not rospy.is_shutdown():
        try:
	    ser = serial.Serial(port, baud_rate)
	    entrada = raw_input("Ingrese una tecla (w/s/a/d) o 'q' para salir: ")

   	    if entrada == 'q':
       		 break  # Salir del bucle si se ingresa 'q'
   	    elif entrada == 'w':
                 valor = 1
            elif entrada == 's':
                 valor = 2
            elif entrada == 'a':
                 valor = 3
            elif entrada == 'd':
                 valor = 4
            else:
                 print("Error: Tecla inválida.")
                 continue  # Volver a solicitar una nueva entrada

	    data_to_send = str(valor)  # Convierte la entrada a una cadena de texto
	    ser.write(data_to_send.encode('utf-8'))  # Codifica la cadena de texto y envía los datos
            ser.close()
	    rospy.loginfo("Conexión con Arduino establecida correctamente")
	    rospy.loginfo("Datos enviados: %s" % data_to_send)

        except serial.SerialException:
            rospy.logerr("No se pudo establecer conexión con el sensor")

        time.sleep(1)  # Esperar 1 segundo antes del siguiente dato

if __name__ == '__main__':
    try:
        read_ultrasound_data()
    except rospy.ROSInterruptException:
        pass
