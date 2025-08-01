#Proyecto Señales Electricas - Año 2025
#Autor: Uberti, Ulises Leandro

#Este archivo permite realizar pruebas sobre los archivos
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#libreria que permite leer y modificar archivos de audio .wav
import wave

#Bloque para determinar las caracterisiticas del archivo de audio

#Funcion para obtener las caracterisiticas del archivo .wav
#Un archivo .wav tiene una estructura llamada "formato RIFF"
#RIFF --> Formato de 
def Audio_Caracteristicas(nombre_archivo):
    with wave.open(nombre_archivo, "rb") as wav_file:
        nchannels = wav_file.getnchannels()
        sampwidth = wav_file.getsampwidth()
        framerate = wav_file.getframerate()
        nframes = wav_file.getnframes() #obtiene la cantidad de muestras (mono: 1 frame -> 1 muestra)
        duration = nframes / framerate # La cantidad de muestras entre la frecuencia de muestreo permite conocer la duracion del audio 

        print(f"Canales: {nchannels}")                   #Cantidad de canales
        print(f"Bits por muestra: {sampwidth * 8}")      #Cantidad de bits por muestra (sampwidth obtiene la cantidad de bytes por muestra)
        print(f"Frecuencia de muestreo: {framerate} Hz") #Frecuencia de muestreo [Hz]
        print(f"Duración: {duration:.2f} segundos")      #Duracion del audio 
        return nchannels, sampwidth * 8, framerate, nframes, duration


#Funcion para graficar la señal de audio 
def Audio_Grafica(nombre_archivo):
    with wave.open(nombre_archivo,"rb") as wav_file:
        nchannels = wav_file.getnchannels() # cantidad de canales
        sampwidth = wav_file.getsampwidth() # cantidad de bytes por muestra 
        framerate = wav_file.getframerate() # frecuencia de muestreo de la señal
        nframes = wav_file.getnframes() #obtiene la cantidad de muestras (mono: 1 frame -> 1 muestra)
        duration = nframes / framerate # La cantidad de muestras entre la frecuencia de muestreo permite conocer la duracion del audio 

        #verifico que la señal sea de un solo canal (mono)
        if nchannels != 1:
            #"raise" permite cortar el flujo de la funcion e indicar error
            raise ValueError("Error en la cantidad de canales de la señal. No es mono")
        
        #leemos los datos del audio como bytes 
        #audio_bytes es un array de bytes 
        audio_bytes = wav_file.readframes(nframes) 
        # distinguimos si se esta trabajando con archivos de 2 bytes o 1 byte
        if sampwidth == 2:
            #audio es un array de numeros enteros con signo correspondiente a cada byte 
            audio = np.frombuffer(audio_bytes,dtype=np.int16)
        elif sampwidth == 1:
            audio = np.frombuffer(audio_bytes,dtype=np.uint8)
        else:
            raise ValueError ("Cantidad de bytes excedentes")
        
        #creamos el arreglo de tiempo para el eje horizontal
        t_audio = np.linspace(start=0,stop=nframes/framerate,num=nframes)

        #graficamos la señal 
        plt.plot(t_audio,audio,'red')
        plt.title("Señal de audio original")
        plt.grid(True)
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Amplitud (bytes a enteros con signo)")
        plt.figure(figsize=(135,20))
        plt.show()


