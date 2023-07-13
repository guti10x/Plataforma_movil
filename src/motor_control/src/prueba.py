#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import serial
import time

def send_data_to_arduino():
    rospy.init_node('data_sender', anonymous=True)

    port = '/dev/ttyACM0'  # Puerto serial al que está conectado el Arduino
    baud_rate = 9600  # Velocidad de comunicación

    try:
        ser = serial.Serial(port, baud_rate)
        rospy.loginfo("Conexión con Arduino establecida correctamente")

        while not rospy.is_shutdown():
            entrada = raw_input("Ingrese la dirección (w, s, a, d): ")
            
            if entrada == 'q':
                break  # Salir del bucle si se ingresa 'q'
            elif entrada == 'w':
                valor = 2
            elif entrada == 's':
                valor = 1
            elif entrada == 'a':
                valor = 3
            elif entrada == 'd':
                valor = 4
            else:
                print("Error: Tecla inválida.")
                continue  # Volver a solicitar una nueva entrada

            ser.write(str(valor).encode('utf-8'))  # Envía el valor codificado en utf-8
            rospy.loginfo("Valor enviado: %d" % valor)

    except serial.SerialException:
        rospy.logerr("No se pudo establecer conexión con el Arduino")

    finally:
        if ser.is_open:
            ser.close()

if __name__ == '__main__':
    try:
        send_data_to_arduino()
    except rospy.ROSInterruptException:
        pass

