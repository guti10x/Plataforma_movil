#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyfirmata import Arduino, util

# Configuración del puerto serial
port = '/dev/ttyACM0'  # Ajusta el puerto serial según corresponda

try:
    # Intenta establecer la conexión con el Arduino
    board = Arduino(port, baudrate=9600, timeout=1)  # Modifica la velocidad de baudios y el tiempo de espera si es necesario
    print("Conexión exitosa con Arduinooooooooo")
    board.exit()  # Cierra la conexión después de verificarla
except Exception as e:
    print("Error al conectar con Arduinooooooooooo:", str(e))
