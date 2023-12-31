#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import serial
import time

def read_ultrasound_data():
    rospy.init_node('ultrasound_data_reader', anonymous=True)

    port = '/dev/ttyACM0'  # Puerto serial al que está conectado el Arduino
    baud_rate = 9600  # Velocidad de comunicación

    while not rospy.is_shutdown():
        try:
            ser = serial.Serial(port, baud_rate)
            data = ser.readline().strip().decode('utf-8')
            ser.close()
            #rospy.loginfo("Conexión con Arduino establecida correctamente")
            rospy.loginfo("Distancia frontal: %s cm." % data)
        except serial.SerialException:
            rospy.logerr("No se pudo establecer conexión con el sensor")

        time.sleep(1)  # Esperar 1 segundo antes de la siguiente lectura

if __name__ == '__main__':
    try:
        read_ultrasound_data()
    except rospy.ROSInterruptException:
        pass
