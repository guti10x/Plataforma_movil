#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import serial
from std_msgs.msg import String

def send_command(command):
    rospy.loginfo("Enviando comando: {}".format(command))
    ser.write(command.encode())  # Enviar el comando al Arduino a través de la comunicación serial

if __name__ == '__main__':
    rospy.init_node('arduino_control_node')
    rospy.loginfo("Nodo de control de Arduino iniciado.")

    # Configurar la comunicación serial con Arduino
    port = '/dev/ttyACM0'  # Puerto serial al que está conectado el Arduino
    baud_rate = 9600  # Velocidad de comunicación
    ser = serial.Serial(port, baud_rate)

    # Crear el publicador para enviar los comandos al Arduino
    pub = rospy.Publisher('arduino_commands', String, queue_size=10)

    while not rospy.is_shutdown():
        # Leer la entrada por consola
        command = raw_input("Introduce un comando (w, a, s, d): ")

        # Publicar el comando
        pub.publish(command)

        # Enviar el comando al Arduino
        send_command(command)

