import random
import string  # Es para todos los elementos en mayúsculas
from lista import lista

class Juego:
    def __init__(self):
        self.palabra = ""
        self.letras_por_adivinar = set()
        self.letras_adivinadas = set()
        self.abecedario = set(string.ascii_uppercase)
        self.vidas = 7

    def iniciar(self):
        print("¡Bienvenido al Juego del Ahorcado!")

        # Obtener una palabra válida de la lista
        self.palabra = self.obtener_palabra_valida(lista)
        self.letras_por_adivinar = set(self.palabra)
        self.letras_adivinadas = set()
        self.vidas = 7

        # Iniciar el bucle de juego
        while len(self.letras_por_adivinar) > 0 and self.vidas > 0:
            self.mostrar_estado_juego()
            letra_usuario = self.obtener_letra_usuario()
            self.actualizar_juego(letra_usuario)

        # Mostrar el resultado al final del juego
        self.mostrar_resultado()

    def obtener_palabra_valida(self, palabras):
        palabra = random.choice(palabras)
        while '_' in palabra or ' ' in palabra:  # Asegurarse de que no sea una palabra inválida
            palabra = random.choice(palabras)
        return palabra.upper()

    def mostrar_estado_juego(self):
        # Mostrar el estado actual del juego
        print(f"\nTe quedan {self.vidas} vidas y has usado estas letras: {' '.join(self.letras_adivinadas)}")
        palabra_mostrada = [letra if letra in self.letras_adivinadas else '_' for letra in self.palabra]
        print(' '.join(palabra_mostrada))

    def obtener_letra_usuario(self):
        # Solicitar una letra al jugador
        while True:
            letra = input("Adivina una letra: ").upper()
            if letra in self.abecedario and letra not in self.letras_adivinadas:
                return letra
            else:
                print("Letra inválida o ya adivinada, intenta de nuevo.")

    def actualizar_juego(self, letra_usuario):
        # Actualizar las letras adivinadas y verificar si la letra está en la palabra
        self.letras_adivinadas.add(letra_usuario)
        if letra_usuario in self.letras_por_adivinar:
            self.letras_por_adivinar.remove(letra_usuario)
        else:
            self.vidas -= 1
            print(f"\nTu letra, '{letra_usuario}', no está en la palabra.")

    def mostrar_resultado(self):
        # Mostrar el resultado final
        if self.vidas == 0:
            print("¡Ahorcado! Perdiste. La palabra era:", self.palabra)
        else:
            print(f"¡Excelente! ¡Adivinaste la palabra: {self.palabra}!")

if __name__ == '__main__':
    juego = Juego()
    juego.iniciar()
