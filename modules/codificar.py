#Proyecto Señales Electricas - Año 2025
#Autor: Uberti, Ulises Leandro
#Codigo fuente de codificar.py

#Este archivo permite realizar la codificacion sobre los una señal cuantificada (audio.wav)
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#libreria que permite leer y modificar archivos de audio .wav
import wave
#Importamos la funcion para obtener las caracterisiticas del archivo .wav
from modules.caracteristicas import Audio_Caracteristicas

def Codificar_Senial(nombre_archivo):
    #obtengo los parametros de la señal de audio
    nchannels, sampwidth , framerate, nframes, duration = Audio_Caracteristicas(nombre_archivo)
    #cortamos flujo de la funcion si la señal tiene mas de un canal
    if nchannels != 1:
        raise ValueError("Error! El canal no es mono")
    #convertimos las muestras del archivo en un arreglo de bytes
    with wave.open(nombre_archivo,'rb') as wav_file:
            #funcion para leer las muestras del archivo, argumento: cantidad de muestras 
            audio_bytes = wav_file.readframes(nframes)
            #print(audio_bytes)
    #Como se trata de 16 bits convierto a enteros 
    audio = np.frombuffer(audio_bytes,dtype=np.int16)   
    # audio es un arreglo de enteros donde cada elemento representa el entero correspondiente a 16 bits

    #Convertimos esos enteros en binario
    #np.binary_repr es una funcion de numpy que convierte un numero en una cada binaria
    #el argumento muestra & 0xFFFF permite convertir numeros con signo
    audio_bits = [np.binary_repr(int(muestra) & 0xFFFF,width=16) for muestra in audio]
    #audio_bits es una cadena de strings donde cada string representa 16 bits
    
    # Convertimos la cadena de strings en un solo arreglo de bits
    # Recorremos la cadena y luego recorremos cada elemento de la cadena
    # dtype= np.int8 es la forma de representar cada bit 
    bits_array = np.array([int(bit) for bits in audio_bits for bit in bits],dtype= np.uint8)

    return bits_array

    


