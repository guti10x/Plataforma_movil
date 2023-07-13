#include <NewPing.h>

const int ledPin = 13; // Pin al que está conectado el LED

// Definición de pines del puente H
#define in1 7
#define in2 8
#define in3 9
#define in4 10
#define enA 6
#define enB 11

#define TRIGGER_PIN 3
#define ECHO_PIN 4
NewPing sonar(TRIGGER_PIN, ECHO_PIN);

String data;
int valor ; 

void setup() {
  
  // Configurar pin del led
  pinMode(ledPin, OUTPUT); // Establece el pin como salida

  // Configurar los pines del puente H como salidas
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);

  // Inicializar velocidad de los motores a 0
  analogWrite(enA, 0);
  analogWrite(enB, 0);

  // Iniciar comunicación serial
  Serial.begin(9600);
}

void moverAdelante() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 255);
  analogWrite(enB, 255);
}

void moverAtras() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enA, 255);
  analogWrite(enB, 255);
}

void moverIzquierda() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enA, 255);
  analogWrite(enB, 255);
}

void moverDerecha() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 255);
  analogWrite(enB, 255);
}

void detener() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(enA, 0);
  analogWrite(enB, 0);
}

void loop() {
  
  unsigned int distance = sonar.ping_cm(); // Realizar la medición de distancia en centímetros

  // Enviar el valor de la distancia a través de la comunicación serial
  Serial.println(distance);

  //if (Serial.available()) {  // Si hay datos disponibles en el puerto serie}
    data = Serial.readStringUntil('\n');  // Lee la cadena de caracteres hasta encontrar un salto de línea
    valor = data.toInt();  // Convierte la cadena a un entero
    
    if (distance < 10 && distance >= 1) {
      // Detener los motores del coche si la distancia es menor a 10 cm
      valor = 5;
    }
   
    if (valor == 1) {
      digitalWrite(ledPin,HIGH ); // Apaga el LED 
      moverAdelante();
    } else if (valor == 2) {
      digitalWrite(ledPin, LOW ); // Enciende el LED
      moverAtras();
    } else if (valor == 3) {
      moverIzquierda();
    } else if (valor == 4) {
      moverIzquierda();
    } else if (valor == 5) {
      detener();
    }
}
