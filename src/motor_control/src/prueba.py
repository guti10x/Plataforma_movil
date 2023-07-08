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
            data_to_send = raw_input("Ingrese los datos a enviar: ")
            ser.write(data_to_send.encode('utf-8'))  # Envía los datos codificados en utf-8
            rospy.loginfo("Datos enviados: %s" % data_to_send)

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

